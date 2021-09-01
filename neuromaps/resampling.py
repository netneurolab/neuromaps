# -*- coding: utf-8 -*-
"""
Functions for comparing data
"""

import nibabel as nib
import numpy as np

from neuromaps import transforms
from neuromaps.datasets import ALIAS, DENSITIES
from neuromaps.images import load_gifti, load_nifti


_resampling_docs = dict(
    resample_in="""\
src, trg : str or os.PathLike or niimg_like or nib.GiftiImage or tuple
    Input data to be resampled
src_space, trg_space : str
    Template space of input data
method : {'nearest', 'linear'}, optional
    Method for resampling. Specify 'nearest' if `data` are label images.
    Default: 'linear'\
""",
    hemi="""\
hemi : {'L', 'R'}, optional
    If `src` and `trg` are not tuples this specifies the hemisphere the data
    represent. Default: None\
""",
    resample_out="""\
src, trg : tuple-of-nib.GiftiImage
    Resampled images\
"""
)


def downsample_only(src, trg, src_space, trg_space, method='linear',
                    hemi=None):
    src_den, trg_den = transforms._estimate_density((src, trg), hemi)
    src_num, trg_num = int(src_den[:-1]), int(trg_den[:-1])
    src_space, trg_space = src_space.lower(), trg_space.lower()

    if src_num >= trg_num:  # resample to `trg`
        func = getattr(transforms, f'{src_space}_to_{trg_space}')
        src = func(src, trg_den, hemi=hemi, method=method)
    elif src_num < trg_num:  # resample to `src`
        func = getattr(transforms, f'{trg_space}_to_{src_space}')
        trg = func(trg, src_den, hemi=hemi, method=method)

    return src, trg


downsample_only.__doc__ = """\
Resamples `src` and `trg` to match such that neither is upsampled

If density of `src` is greater than `trg` then `src` is resampled to
`trg`; otherwise, `trg` is resampled to `src`

Parameters
----------
{resample_in}
{hemi}

Returns
-------
{resample_out}
""".format(**_resampling_docs)


def transform_to_src(src, trg, src_space, trg_space, method='linear',
                     hemi=None):
    src_den, trg_den = transforms._estimate_density((src, trg), hemi)

    func = getattr(transforms, f'{trg_space.lower()}_to_{src_space.lower()}')
    trg = func(trg, src_den, hemi=hemi, method=method)

    return src, trg


transform_to_src.__doc__ = """\
Resamples `trg` to match space and density of `src`

Parameters
----------
{resample_in}
{hemi}

Returns
-------
{resample_out}
""".format(**_resampling_docs)


def transform_to_trg(src, trg, src_space, trg_space, hemi=None,
                     method='linear'):
    src_den, trg_den = transforms._estimate_density((src, trg), hemi)

    func = getattr(transforms, f'{src_space.lower()}_to_{trg_space.lower()}')
    src = func(src, trg_den, hemi=hemi, method=method)

    return src, trg


transform_to_trg.__doc__ = """\
Resamples `trg` to match space and density of `src`

Parameters
----------
{resample_in}

Returns
-------
{resample_out}
""".format(**_resampling_docs)


def transform_to_alt(src, trg, src_space, trg_space, method='linear',
                     hemi=None, alt_space='fsaverage', alt_density='41k'):
    src, _ = transform_to_trg(src, alt_density, src_space, alt_space,
                              hemi=hemi, method=method)
    trg, _ = transform_to_trg(trg, alt_density, trg_space, alt_space,
                              hemi=hemi, method=method)

    return src, trg


transform_to_alt.__doc__ = """\
Resamples `src` and `trg` to `alt_space` and `alt_density`

Parameters
----------
{resample_in}
{hemi}
alt_space : {{'fsaverage', 'fsLR', 'civet'}}, optional
    Alternative space to which `src` and `trg` should be transformed. Default:
    'fsaverage'
alt_density : str, optional
    Resolution to which `src` and `trg` should be resampled. Must be valid
    with `alt_space`. Default: '41k'

Returns
-------
{resample_out}
""".format(**_resampling_docs)


def mni_transform(src, trg, src_space, trg_space, method='linear', hemi=None):
    if src_space != 'MNI152':
        raise ValueError('Cannot perform MNI transformation when src_space is '
                         f'not "MNI152." Received: {src_space}.')
    trg_den = trg
    if trg_space != 'MNI152':
        trg_den, = transforms._estimate_density((trg_den,), hemi)
    func = getattr(transforms, f'mni152_to_{trg_space.lower()}')
    src = func(src, trg_den, method=method)

    return src, trg


mni_transform.__doc__ = """\
Resamples `src` in MNI152 to `trg` space

Parameters
----------
{resample_in}
hemi : {{'L', 'R'}}, optional
    If `trg_space` is not "MNI152' and `trg` is not a tuple this specifies the
    hemisphere the data represent. Default: None

Returns
-------
{resample_out}
""".format(**_resampling_docs)


def _check_altspec(spec):
    """
    Confirms that specified alternative `spec` is valid (space, density) format

    Parameters
    ----------
    spec : (2,) tuple-of-str
        Where entries are (space, density) of desired target space

    Returns
    -------
    spec : (2,) tuple-of-str
        Unmodified input `spec`

    Raises
    ------
    ValueError
        If `spec` is not valid format
    """

    invalid_spec = spec is None or len(spec) != 2
    if not invalid_spec:
        space, den = spec
        space = ALIAS.get(space, space)
        valid = DENSITIES.get(space)
        invalid_spec = valid is None or den not in valid
    if invalid_spec:
        raise ValueError('Must provide valid alternative specification of '
                         f'format (space, density). Received: {spec}')

    return (space, den)


def resample_images(src, trg, src_space, trg_space, method='linear',
                    hemi=None, resampling='downsample_only', alt_spec=None):

    resamplings = ('downsample_only', 'transform_to_src', 'transform_to_trg',
                   'transform_to_alt')
    if resampling not in resamplings:
        raise ValueError(f'Invalid method: {resampling}')

    src_space = ALIAS.get(src_space, src_space)
    trg_space = ALIAS.get(trg_space, trg_space)

    # all this input handling just to deal with volumetric images :face_palm:
    opts, err = {}, None
    if resampling == 'transform_to_alt':
        opts['alt_space'], opts['alt_density'] = _check_altspec(alt_spec)
        if (opts['alt_space'] == 'MNI152'
                and (src_space != 'MNI152' or trg_space != 'MNI152')):
            raise ValueError('Cannot transform to "MNI152" system if either '
                             '`src` or `trg` are not in "MNI152" system.')
    elif (resampling == 'transform_to_src' and src_space == 'MNI152'
            and trg_space != 'MNI152'):
        err = ('Specified `src_space` cannot be "MNI152" when `resampling` is '
               '"transform_to_src"')
    elif (resampling == 'transform_to_trg' and src_space != 'MNI152'
            and trg_space == 'MNI152'):
        err = ('Specified `trg_space` cannot be "MNI152" when `resampling` is '
               '"transform_to_trg"')
    elif (resampling == 'transform_to_alt' and opts['alt_space'] == 'MNI152'
            and (src_space != 'MNI152' or trg_space != 'MNI152')):
        err = ('Specified `alt_space` cannot be "MNI152" when `resampling` is '
               '"transform_to_alt"')
    if err is not None:
        raise ValueError(err)

    # handling volumetric data is annoying...
    if ((src_space == "MNI152" or trg_space == "MNI152")
            and resampling == 'transform_to_alt'):
        func = mni_transform if src_space == 'MNI152' else transform_to_trg
        src = func(src, opts['alt_density'], src_space, opts['alt_space'],
                   method=method, hemi=hemi)[0]
        func = mni_transform if trg_space == 'MNI152' else transform_to_trg
        trg = func(trg, opts['alt_density'], trg_space, opts['alt_space'],
                   method=method, hemi=hemi)[0]
    elif src_space == 'MNI152' and trg_space != 'MNI152':
        src, trg = mni_transform(src, trg, src_space, trg_space,
                                 method=method, hemi=hemi)
    elif trg_space == 'MNI152' and src_space != 'MNI152':
        trg, src = mni_transform(trg, src, trg_space, src_space,
                                 method=method, hemi=hemi)
    elif src_space == 'MNI152' and src_space == 'MNI152':
        src, trg = load_nifti(src), load_nifti(trg)
        srcres = np.prod(nib.affines.voxel_sizes(src.affine))
        trgres = np.prod(nib.affines.voxel_sizes(trg.affine))
        if ((resampling == 'downsample_only' and srcres > trgres)
                or resampling == 'transform_to_src'):
            trg, src = mni_transform(trg, src, trg_space, src_space,
                                     method=method)
        elif ((resampling == 'downsample_only' and srcres <= trgres)
                or resampling == 'transform_to_trg'):
            src, trg = mni_transform(src, trg, src_space, trg_space,
                                     method=method)
    else:
        func = globals()[resampling]
        src, trg = func(src, trg, src_space, trg_space, hemi=hemi,
                        method=method, **opts)
        src = tuple(load_gifti(s) for s in src)
        trg = tuple(load_gifti(t) for t in trg)

    return src, trg


resample_images.__doc__ = """\
Resamples images `src` and `trg` to same space/density with `resampling` method

Parameters
----------
{resample_in}
{hemi}
resampling : str, optional
    Name of resampling function to resample `src` and `trg`. Must be one of:
    'downsample_only', 'transform_to_src', 'transform_to_trg',
    'transform_to_alt'. See Notes for more info. Default: 'downsample_only'
alt_spec : (2,) tuple-of-str
    Where entries are (space, density) of desired target space. Only used if
    `resampling='transform_to_alt'`. Default: None

Returns
-------
{resample_out}

Notes
-----
The four available `resampling` strategies will control how `src` and/or `trg`
are resampled prior to correlation. Options include:

    1. `resampling='downsample_only'`

    Data from `src` and `trg` are resampled to the lower resolution of the two
    input datasets

    2. `resampling='transform_to_src'`

    Data from `trg` are always resampled to match `src` space and resolution

    3. `resampling='transform_to_trg'`

    Data from `src` are always resampled to match `trg` space and resolution

    4. `resampling='transform_to_alt'`

    Data from `trg` and `src` are resampled to the space and resolution
    specified by `alt_spec` (space, density)

""".format(**_resampling_docs)
