# -*- coding: utf-8 -*-
"""
Functionality for transforming files between spaces
"""

import os
from pathlib import Path

import nibabel as nib
from nilearn import image as nimage
import numpy as np
from scipy.interpolate import interpn

from brainnotation.datasets import (ALIAS, DENSITIES, fetch_atlas,
                                    fetch_regfusion, get_atlas_dir)
from brainnotation.images import construct_shape_gii, load_gifti
from brainnotation.utils import tmpname, run

METRICRESAMPLE = 'wb_command -metric-resample {metric} {src} {trg} ' \
                 'ADAP_BARY_AREA {out} -area-metrics {srcarea} {trgarea} ' \
                 '-current-roi {srcmask}'
LABELRESAMPLE = 'wb_command -label-resample {metric} {src} {trg} ' \
                'ADAP_BARY_AREA {out} -area-metrics {srcarea} {trgarea} ' \
                '-current-roi {srcmask}'
MASKSURF = 'wb_command -metric-mask {out} {trgmask} {out}'
SURFFMT = 'tpl-{space}{trg}_den-{den}_hemi-{hemi}_sphere.surf.gii'
VAFMT = 'tpl-{space}_den-{den}_hemi-{hemi}_desc-vaavg_midthickness.shape.gii'
MLFMT = 'tpl-{space}_den-{den}_hemi-{hemi}_desc-nomedialwall_dparc.label.gii'


def _regfusion_project(data, ras, affine, method='linear'):
    """
    Project `data` to `ras` space using regfusion

    Parameters
    ----------
    data : (X, Y, Z[, V]) array_like
        Input (volumetric) data to be projected to the surface
    ras : (N, 3) array_like
        Coordinates of surface points derived from registration fusion
    affine (4, 4) array_like
        Affine mapping `data` to `ras`-space coordinates
    method : {'nearest', 'linear'}, optional
        Method for projection. Default: 'linear'

    Returns
    -------
    projected : (N, V) array_like
        Input `data` projected to the surface
    """

    data, ras, affine = np.asarray(data), np.asarray(ras), np.asarray(affine)
    coords = nib.affines.apply_affine(np.linalg.inv(affine), ras)
    volgrid = [range(data.shape[i]) for i in range(3)]
    if data.ndim == 3:
        projected = interpn(volgrid, data, coords, method=method)
    elif data.ndim == 4:
        projected = np.column_stack([
            interpn(volgrid, data[..., n], coords, method=method)
            for n in range(data.shape[-1])
        ])

    return construct_shape_gii(projected.squeeze())


def _vol_to_surf(img, space, density, method='linear'):
    """
    Projects `img` to the surface defined by `space` and `density`

    Parameters
    ----------
    img : niimg_like, str, or os.PathLike
        Image to be projected to the surface
    den : str
        Density of desired output space
    space : str
        Desired output space
    method : {'nearest', 'linear'}, optional
        Method for projection. Default: 'linear'

    Returns
    -------
    projected : (2,) tuple-of-nib.GiftiImage
        Left [0] and right [1] hemisphere projected `image` data
    """

    space = ALIAS.get(space, space)
    if space not in DENSITIES:
        raise ValueError(f'Invalid space argument: {space}')
    if density not in DENSITIES[space]:
        raise ValueError(f'Invalid density for {space} space: {density}')
    if method not in ('nearest', 'linear'):
        raise ValueError('Invalid method argument: {method}')

    if isinstance(img, (str, os.PathLike)):
        img = nib.load(img)

    out = ()
    for ras in fetch_regfusion(space)[density]:
        out += (_regfusion_project(img.get_fdata(), np.loadtxt(ras),
                                   img.affine, method=method),)

    return out


def mni152_to_civet(img, civet_density='41k', method='linear'):
    """
    Projects `img` in MNI152 space to CIVET surface

    Parameters
    ----------
    img : str or os.PathLike or niimg_like
        Image in MNI152 space to be projected
    civet_density : {'41k'}, optional
        Desired output density of CIVET surface. Default: '41k'
    method : {'nearest', 'linear'}, optional
        Method for projection. Specify 'nearest' if `img` is a label image.
        Default: 'linear'

    Returns
    -------
    civet : (2,) tuple-of-nib.GiftiImage
        Projected `img` on CIVET surface
    """

    if civet_density == '164k':
        raise NotImplementedError('Cannot perform registration fusion to '
                                  'CIVET 164k space yet.')

    return _vol_to_surf(img, 'civet', civet_density, method)


def mni152_to_fsaverage(img, fsavg_density='41k', method='linear'):
    """
    Projects `img` in MNI152 space to fsaverage surface

    Parameters
    ----------
    img : str or os.PathLike or niimg_like
        Image in MNI152 space to be projected
    fsavg_density : {'3k', '10k', '41k', '164k'}, optional
        Desired output density of fsaverage surface. Default: '41k'
    method : {'nearest', 'linear'}, optional
        Method for projection. Specify 'nearest' if `img` is a label image.
        Default: 'linear'

    Returns
    -------
    fsaverage : (2,) tuple-of-nib.GiftiImage
        Projected `img` on fsaverage surface
    """

    return _vol_to_surf(img, 'fsaverage', fsavg_density, method)


def mni152_to_fslr(img, fslr_density='32k', method='linear'):
    """
    Projects `img` in MNI152 space to fsLR surface

    Parameters
    ----------
    img : str or os.PathLike or niimg_like
        Image in MNI152 space to be projected
    fslr_density : {'32k', '164k'}, optional
        Desired output density of fsLR surface. Default: '32k'
    method : {'nearest', 'linear'}, optional
        Method for projection. Specify 'nearest' if `img` is a label image.
        Default: 'linear'

    Returns
    -------
    fsLR : (2,) tuple-of-nib.GiftiImage
        Projected `img` on fsLR surface
    """

    if fslr_density in ('4k', '8k'):
        raise NotImplementedError('Cannot perform registration fusion to '
                                  f'fsLR {fslr_density} space yet.')

    return _vol_to_surf(img, 'fsLR', fslr_density, method)


def mni152_to_mni152(img, target=None, resolution='1mm', method='linear'):
    """
    Resamples `img` to `target` image (if supplied) or target `resolution`

    Parameters
    ----------
    img : str or os.PathLike or niimg_like
        Image in MNI152 space to be resampled
    target : str or os.PathLike or niimg_like
        Image in MNI152 space to which `img` should be resampled. If not
        specified `resolution` is used instead. Default: None
    resolution : {'1mm', '2mm', '3mm'}, optional
        Desired resolution of output resampled image. Ignored if `target` is
        specified. Default: '1mm'
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `img` is a label image.
        Default: 'linear'

    Returns
    -------
    resampled : nib.Nifti1Image
        Resampled input `img`
    """

    if resolution not in DENSITIES['MNI152']:
        raise ValueError(f'Invalid target resolution: {resolution}')
    res = int(resolution[0])

    if target is not None:
        out = nimage.resample_to_img(img, target, interpolation=method)
    else:
        out = nimage.resample_img(img, np.eye(3) * res, interpolation=method)

    return out


def _check_hemi(data, hemi):
    """ Utility to check that `data` and `hemi` jibe

    Parameters
    ----------
    data : str or os.PathLike or tuple
        Input data
    hemi : str
        Hemisphere(s) corresponding to `data

    Returns
    -------
    zipped : zip
        Zipped instance of `data` and `hemi`
    """

    if isinstance(data, (str, os.PathLike)) or not hasattr(data, '__len__'):
        data = (data,)
    if len(data) == 1 and hemi is None:
        raise ValueError('Must specify `hemi` when only 1 data file supplied')
    if hemi is not None and isinstance(hemi, str) and hemi not in ('L', 'R'):
        raise ValueError(f'Invalid hemisphere designation: {hemi}')
    elif hemi is not None and isinstance(hemi, str):
        hemi = (hemi,)
    elif hemi is not None and any(h not in ('L', 'R') for h in hemi):
        raise ValueError(f'Invalid hemisphere designations: {hemi}')
    else:
        hemi = ('L', 'R')

    return zip(data, hemi)


def _surf_to_surf(data, srcparams, trgparams, method='linear', hemi=None):
    """
    Resamples surface `data` to another surface

    Parameters
    ----------
    data : str or os.Pathlike or tuple
        Filepath(s) to data. If not a tuple then `hemi` must be specified. If
        a tuple then it is assumed that files are ('left', 'right')
    srcparams, trgparams : dict
        Dictionary with keys ['space', 'den', 'trg']
    method : {'nearest', 'linear'}, optional
        Method for resampling. Default: 'linear'
    hemi : str or None
        Hemisphere of `data` if `data` is a single image. Default: None

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new surface
    """

    methods = ('nearest', 'linear')
    if method not in methods:
        raise ValueError(f'Invalid method: {method}. Must be one of {methods}')

    keys = ('space', 'den', 'trg')
    for key in keys:
        if key not in srcparams:
            raise KeyError(f'srcparams missing key: {key}')
        if key not in trgparams:
            raise KeyError(f'trgparams missing key: {key}')

    for val in (srcparams, trgparams):
        space, den = val['space'], val['den']
        if den not in DENSITIES[space]:
            raise ValueError(f'Invalid density for {space} space: {den}')

    # if our source and target are identical just return the loaded data
    if srcparams == trgparams:
        data, _ = zip(*_check_hemi(data, hemi))
        return tuple(load_gifti(d) for d in data)

    # get required atlas / templates for transforming between spaces
    for atl in (srcparams, trgparams):
        fetch_atlas(atl['space'], atl['den'])
    srcdir = get_atlas_dir(srcparams['space'])
    trgdir = get_atlas_dir(trgparams['space'])

    resampled = ()
    func = METRICRESAMPLE if method == 'linear' else LABELRESAMPLE
    for img, hemi in _check_hemi(data, hemi):
        srcparams['hemi'] = trgparams['hemi'] = hemi
        try:
            img = Path(img).resolve()
            tmpimg = None
        except TypeError:
            tmpimg = tmpname(suffix='.gii')
            nib.save(img, tmpimg)
            img = Path(tmpimg).resolve()
        params = dict(
            metric=img,
            out=tmpname('.func.gii'),
            src=srcdir / SURFFMT.format(**srcparams),
            trg=trgdir / SURFFMT.format(**trgparams),
            srcarea=srcdir / VAFMT.format(**srcparams),
            trgarea=trgdir / VAFMT.format(**trgparams),
            srcmask=srcdir / MLFMT.format(**srcparams),
            trgmask=trgdir / MLFMT.format(**trgparams)
        )
        for fn in (func, MASKSURF):
            run(fn.format(**params), quiet=True)
        resampled += (construct_shape_gii(
            load_gifti(params['out']).agg_data()
        ),)
        params['out'].unlink()
        if tmpimg is not None:
            tmpimg.unlink()

    return resampled


def civet_to_fslr(data, density, fslr_density='32k', hemi=None,
                  method='linear'):
    """
    Resamples `data` on CIVET surface to the fsLR surface

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input CIVET data to be resampled to fsLR surface
    density : {'41k', '164k'}
        Resolution of provided `data`
    fslr_density : {'4k', '8k', '32k', '164k'}, optional
        Desired density of output fsLR surface. Default: '32k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new surface
    """

    srcparams = dict(space='civet', den=density, trg='_space-fsLR')
    trgparams = dict(space='fsLR', den=fslr_density, trg='')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)


def fslr_to_civet(data, density, civet_density='41k', hemi=None,
                  method='linear'):
    """
    Resamples `data` on fsLR surface to the CIVET surface

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input fsLR data to be resampled to CIVET surface
    density : {'4k', '8k', '32k', '164k'}
        Resolution of provided `data`
    civet_density : {'41k', '164k'}, optional
        Desired density of output CIVET surface. Default: '41k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new surface
    """

    srcparams = dict(space='fsLR', den=density, trg='')
    trgparams = dict(space='civet', den=civet_density, trg='_space-fsLR')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)


def civet_to_fsaverage(data, density, fsavg_density='41k', hemi=None,
                       method='linear'):
    """
    Resamples `data` on CIVET surface to the fsaverage surface

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input CIVET data to be resampled to fsaverage surface
    density : {'41k', '164k'}
        Resolution of provided `data`
    fsavg_density : {'3k', '10k', '41k', '164k'}, optional
        Desired density of output fsaverage surface. Default: '32k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new surface
    """

    srcparams = dict(space='civet', den=density, trg='_space-fsaverage')
    trgparams = dict(space='fsaverage', den=fsavg_density, trg='')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)


def fsaverage_to_civet(data, density, civet_density='41k', hemi=None,
                       method='linear'):
    """
    Resamples `data` on fsaverage surface to the CIVET surface

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input fsaverage data to be resampled to CIVET surface
    density : {'3k', '10k', '41k', '164k'}
        Resolution of provided `data`
    civet_density : {'41k', '164k'}, optional
        Desired density of output CIVET surface. Default: '41k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new surface
    """

    srcparams = dict(space='fsaverage', den=density, trg='')
    trgparams = dict(space='civet', den=civet_density, trg='_space-fsaverage')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)


def fslr_to_fsaverage(data, density, fsavg_density='41k', hemi=None,
                      method='linear'):
    """
    Resamples `data` on fsLR surface to the fsaverage surface

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input fsLR data to be resampled to fsaverage surface
    density : {'4k', '8k', '32k', '164k'}
        Resolution of provided `data`
    fsavg_density : {'3k', '10k', '41k', '164k'}, optional
        Desired density of output fsaverage surface. Default: '41k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new surface
    """

    srcparams = dict(space='fsLR', den=density, trg='_space-fsaverage')
    trgparams = dict(space='fsaverage', den=fsavg_density, trg='')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)


def fsaverage_to_fslr(data, density, fslr_density='32k', hemi=None,
                      method='linear'):
    """
    Resamples `data` on fsaverage surface to the fsLR surface

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input fsaverage data to be resampled to fsLR surface
    density : {'3k', '10k', '41k', '164k'}
        Resolution of provided `data`
    fslr_density : {'4k', '8k', '32k', '164k'}, optional
        Desired density of output fsLR surface. Default: '32k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new surface
    """

    srcparams = dict(space='fsaverage', den=density, trg='')
    trgparams = dict(space='fsLR', den=fslr_density, trg='_space-fsaverage')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)


def civet_to_civet(data, density, civet_density='41k', hemi=None,
                   method='linear'):
    """
    Resamples `data` on CIVET surface to new density

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input CIVET data to be resampled
    density : {'41k', '164k'}
        Resolution of provided `data`
    civet_density : {'41k', '164k'}, optional
        Desired density of output surface. Default: '41k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new surface
    """

    srcparams = dict(space='civet', den=density, trg='')
    trgparams = dict(space='civet', den=civet_density, trg='')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)


def fslr_to_fslr(data, density, fslr_density='32k', hemi=None,
                 method='linear'):
    """
    Resamples `data` on fsLR surface to new density

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input fsLR data to be resampled
    density : {'4k', '8k', '32k', '164k'}
        Resolution of provided `data`
    fslr_density : {'4k', '8k', '32k', '164k'}, optional
        Desired density of output surface. Default: '32k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new density
    """

    srcparams = dict(space='fsLR', den=density, trg='')
    trgparams = dict(space='fsLR', den=fslr_density, trg='')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)


def fsaverage_to_fsaverage(data, density, fsavg_density='41k', hemi=None,
                           method='linear'):
    """
    Resamples `data` on fsaverage surface to new density

    Parameters
    ----------
    data : str or os.PathLike or nib.GiftiImage or tuple
        Input fsaverage data to be resampled
    density : {'3k', '10k', '41k', '164k'}
        Resolution of provided `data`
    fsavg_density : {'3k', '10k', '41k', '164k'}, optional
        Desired density of output surface. Default: '41k'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple this specifies the hemisphere the data are
        representing. Default: None
    method : {'nearest', 'linear'}, optional
        Method for resampling. Specify 'nearest' if `data` are label images.
        Default: 'linear'

    Returns
    -------
    resampled : tuple-of-nib.GiftiImage
        Input `data` resampled to new density
    """

    srcparams = dict(space='fsaverage', den=density, trg='')
    trgparams = dict(space='fsaverage', den=fsavg_density, trg='')
    return _surf_to_surf(data, srcparams, trgparams, method, hemi)
