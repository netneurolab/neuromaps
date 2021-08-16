# -*- coding: utf-8 -*-
"""
Functions for working with CIVET data
"""

import os

import numpy as np

from neuromaps.points import get_shared_triangles, which_triangle


def read_civet_surf(fname):
    """
    Reads a CIVET-style .obj geometry file

    Parameters
    ----------
    fname : str or os.PathLike
        Filepath to .obj file

    Returns
    -------
    vertices : (N, 3)
        Vertices of surface mesh
    triangles : (T, 3)
        Triangles comprising surface mesh
    """

    k, polygons = 0, []
    with open(fname, 'r') as src:
        n_vert = int(src.readline().split()[6])
        vertices = np.zeros((n_vert, 3))
        for i, line in enumerate(src):
            if i < n_vert:
                vertices[i] = [float(i) for i in line.split()]
            elif i >= (2 * n_vert) + 5:
                if not line.strip():
                    k = 1
                elif k == 1:
                    polygons.extend([int(i) for i in line.split()])

    triangles = np.reshape(np.asarray(polygons), (-1, 3))

    return vertices, triangles


def read_surfmap(surfmap):
    """
    Reads surface map from CIVET

    Parameters
    ----------
    surfmap : str or os.PathLike
        Surface mapping file to be loaded

    Returns
    -------
    control : (N,) array_like
        Control vertex IDs
    v0, v1 : (N,) array_like
        Target vertex IDs
    t : (N, 3) array_like
        Resampling weights
    """

    control, v0, v1, t1, t2 = np.loadtxt(surfmap, skiprows=4).T
    control = control.astype(int)
    v0 = v0.astype(int)
    v1 = v1.astype(int)
    t0 = 1 - t1 - t2

    return control, v0, v1, np.column_stack((t0, t1, t2))


def resample_surface_map(source, morph, target, surfmap):
    """
    Resamples `morph` data defined on `source` surface to `target` surface

    Uses `surfmap` to define mapping

    Inputs
    ------
    source : str or os.PathLike
        Path to surface file on which `morph` is defined
    morph : str or os.PathLike
        Path to morphology data defined on `source` surface
    target : str or os.PathLike
        Path to surface file on which to resample `morph` data
    surfmap : str or os.PathLike
        Path to surface mapping file defining transformation (CIVET style)

    Returns
    -------
    resampled : np.ndarray
        Provided `morph` data resampled to `target` surface
    """

    if isinstance(source, (str, os.PathLike)):
        source = read_civet_surf(source)
    if isinstance(morph, (str, os.PathLike)):
        morph = np.loadtxt(morph)
    if len(morph) != len(source[0]):
        raise ValueError('Provided `morph` file has different number of '
                         'vertices from provided `source` surface')

    if isinstance(target, (str, os.PathLike)):
        target = read_civet_surf(target)
    if isinstance(surfmap, (str, os.PathLike)):
        surfmap = read_surfmap(surfmap)
    if len(surfmap[0]) != len(target[0]):
        raise ValueError('Provided `target` surface has different number of '
                         'vertices from provided `surfmap` transformation.')

    source_tris = get_shared_triangles(source[1])
    resampled = np.zeros_like(morph)
    for (control, v0, v1, t) in zip(*surfmap):
        tris = source_tris[(v0, v1) if v0 < v1 else (v1, v0)]
        point, verts = target[0][control], source[0][tris]
        idx = which_triangle(point, verts)
        if idx is None:
            idx = np.argmin(np.linalg.norm(point - verts[:, -1], axis=1))
        resampled[control] = np.sum(morph[[v0, v1, tris[idx][-1]]] * t)

    return resampled
