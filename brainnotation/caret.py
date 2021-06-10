# -*- coding: utf-8 -*-
"""
CARET files I/O
"""

from io import BytesIO
import re
import struct

import nibabel as nib
import numpy as np


def read_surface_shape(fn):
    """
    Reads surface_shape CARET file

    Parameters
    ----------
    fn : str
        Filepath to surface_shape file

    Returns
    -------
    names : (F,) list-of-str
        Names of columns in `data`
    data : (N, F) np.ndarray
        Data from `fn`
    """

    with open(fn, 'rb') as src:
        surfshape = src.read()
    msg = b'BEGIN-DATA\n'
    offset = surfshape.find(msg) + len(msg)
    header, data = surfshape[:offset].decode(), surfshape[offset:]
    n_nodes = int(re.search(r'tag-number-of-nodes (\d+)', header).group(1))
    n_cols = int(re.search(r'tag-number-of-columns (\d+)', header).group(1))
    names = re.findall(r'tag-column-name \d+ ([\S\s][^\n]*)', header)
    encoding = re.search(r'encoding (\S+)', header).group(1)
    if encoding == 'ASCII':
        data = np.loadtxt(BytesIO(data))
    else:
        data = np.asarray(struct.unpack('>' + ('f' * n_cols * n_nodes), data))
        data = data.reshape(-1, n_cols)
    return names, data


def read_coords(fn):
    """
    Reads coords CARET file

    Parameters
    ----------
    fn : str
        Filepath to coords file

    Returns
    -------
    coords : (N, 3) np.ndarray
        Coordinates from `fn`
    """

    with open(fn, 'rb') as src:
        coords = src.read()
    msg = b'EndHeader\n'
    offset = coords.find(msg) + len(msg)
    _, data = coords[:offset].decode(), coords[offset:]
    n_nodes, = struct.unpack('>i', data[:4])
    data = np.asarray(struct.unpack('>' + 'fff' * n_nodes, data[4:]))
    data = data.reshape(-1, 3)
    return data


def read_topo(fn):
    """
    Reads topo CARET file

    Parameters
    ----------
    fn : str
        Filepath to topo file

    Returns
    -------
    topo : (T, 3) np.ndarray
        Topology from `fn`
    """

    with open(fn, 'rb') as src:
        topo = src.read()
    msg = b'tag-version 1\n'
    if msg not in topo:
        raise ValueError('Cannot load topology data in old format')
    offset = topo.find(msg) + len(msg)
    header, data = topo[:offset].decode(), topo[offset:]
    encoding = re.search(r'encoding (\S+)', header).group(1)
    if encoding == "ASCII":
        data = np.loadtxt(BytesIO('\n'.join(data.split('\n')[1:])))
    else:
        n_nodes, = struct.unpack('>i', data[:4])
        data = np.asarray(struct.unpack('>' + 'iii' * n_nodes, data[4:]))
        data = data.reshape(-1, 3)
    return data


def read_deform_map(fn):
    """
    Reads deform_map CARET file

    Parameters
    ----------
    fn : str
        Filepath to deform_map file

    Returns
    -------
    nodes : (N, 3) np.ndarray
        Neighboring nodes for surface
    barycentric : (N, 3) np.ndarray
        Barycentric coordinates for surface
    """

    with open(fn, 'rb') as src:
        deform = src.read()
    msg = b'DATA-START\n'
    offset = deform.find(msg) + len(msg)
    header, data = deform[:offset].decode(), deform[offset:]
    encoding = re.search(r'encoding (\S+)', header).group(1)
    if encoding == 'ASCII':
        data = np.loadtxt(BytesIO(data))
    else:
        n_nodes, = struct.unpack('>i', data[:4])
        data = np.asarray(struct.unpack('>' + 'iiifff' * n_nodes, data[4:]))
        data = data.reshape(-1, 6)
    nodes, barycentric = data[:, :3].astype(int), data[:, 3:]
    return nodes, barycentric


def apply_deform_map(source, deformation, method='nearest'):
    """
    Applies `deformation` map to `source` brainmap

    Parameters
    ----------
    source : str or os.PathLike
        Path to (gifti) file, to be deformed
    deformation : str or os.PathLike
        Path to deformation map
    methods : {'nearest'}, optional
        Method for applying `deformation` to `source`. Currently only 'nearest'
        is supported. Default: 'nearest'

    Returns
    -------
    projected : (N,) np.ndarray
        Data from `source` projected to surface specified in `deformation`
    """

    methods = {'nearest'}
    if method not in methods:
        raise ValueError(f'Invalid method {method}. Must be one of {methods}')

    nodes, bary = read_deform_map(deformation)
    data = nib.load(source).agg_data()

    if method == 'average':  # FIXME: this is wrong.
        projected = np.sum(data[nodes] * bary, axis=1)
    elif method == 'nearest':
        projected = data[nodes[:, 0]]

    return projected
