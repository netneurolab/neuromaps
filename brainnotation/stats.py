# -*- coding: utf-8 -*-
"""
Functions for statistical analyses
"""

from typing import Iterable

import nibabel as nib
import numpy as np
from scipy.stats import rankdata

from brainnotation.images import load_gifti


def _load_data(data):
    """ Small utility to load + stack `data` images (gifti / nifti)
    """

    out = ()
    for img in data:
        try:
            out += (load_gifti(img).agg_data(),)
        except (AttributeError, TypeError):
            if isinstance(img, str):
                img = nib.load(img)
            out += (img.get_fdata(),)
    return np.hstack(out)


def correlate_images(src, trg, corrtype='pearsonr', ignore_zero=True):
    """
    Correlates images `src` and `trg`

    If `src` and `trg` represent data from multiple hemispheres the data are
    concatenated across hemispheres prior to correlation

    Parameters
    ----------
    src, trg : str or os.PathLike or nib.GiftiImage or niimg_like or tuple
        Images to be correlated
    corrtype : {'pearsonr', 'spearmanr'}, optional
        Type of correlation to perform. Default: 'pearsonr'
    ignore_zero : bool, optional
        Whether to perform correlations ignoring all zero values in `src` and
        `trg` data. Default: True

    Returns
    -------
    correlation : float
         Correlation between `src` and `trg`
    """

    methods = ('pearsonr', 'spearmanr')
    if corrtype not in methods:
        raise ValueError(f'Invalid method: {corrtype}')

    if isinstance(src, str) or not isinstance(src, Iterable):
        src = (src,)
    if isinstance(trg, str) or not isinstance(trg, Iterable):
        trg = (trg,)

    srcdata = _load_data(src)
    trgdata = _load_data(trg)

    if ignore_zero:
        mask = np.logical_or(np.isclose(srcdata, 0), np.isclose(trgdata, 0))
        srcdata, trgdata = srcdata[~mask], trgdata[~mask]

    # drop NaNs
    mask = np.logical_or(np.isnan(srcdata), np.isnan(trgdata))
    srcdata, trgdata = srcdata[~mask], trgdata[~mask]

    if corrtype == 'spearmanr':
        srcdata, trgdata = rankdata(srcdata), trgdata(rankdata)

    return np.corrcoef(srcdata, trgdata)[0, 1]


def resample_and_correlate(src, trg, src_space, trg_space, method='linear',
                           hemi=None, resampling='downsample_only',
                           alt_spec=None, corrtype='pearsonr',
                           ignore_zero=True, nulls=None, parcellation=None):

    raise NotImplementedError
