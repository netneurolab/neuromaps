# -*- coding: utf-8 -*-
"""
Functions for statistical analyses
"""

from functools import partial

import numpy as np
from scipy import special, stats as sstats
try:
    from scipy.stats._stats_py import _chk2_asarray  # scipy >= 1.8.0
except ImportError:
    from scipy.stats.stats import _chk2_asarray  # scipy < 1.8.0
from sklearn.utils.validation import check_random_state

from neuromaps.images import load_data


def compare_images(src, trg, metric='pearsonr', ignore_zero=True, nulls=None,
                   nan_policy='omit'):
    """
    Compares images `src` and `trg`

    If `src` and `trg` represent data from multiple hemispheres the data are
    concatenated across hemispheres prior to comparison

    Parameters
    ----------
    src, trg : tuple or str or os.PathLike or img_like or array-like
        Images (nib.Nifti1Image or nib.GiftiImage) or parcellated data
        to be compared.
    metric : {'pearsonr', 'spearmanr', callable}, optional
        Type of similarity metric to use to compare `src` and `trg` images. If
        a callable function is provided it must accept two inputs and return a
        single value (the similarity metric). Default: 'pearsonr'
    ignore_zero : bool, optional
        Whether to perform comparisons ignoring all zero values in `src` and
        `trg` data. Default: True
    nulls : array_like, optional
        Null data for `src` to use in generating a non-parametric p-value.
        If not specified a parameteric p-value is generated. Default: None
    nan_policy : {'propagate', 'raise', 'omit'}, optional
        Defines how to handle when input contains nan. 'propagate' returns nan,
        'raise' throws an error, 'omit' performs the calculations ignoring nan
        values. Default: 'omit'

    Returns
    -------
    similarity : float
         Comparison metric between `src` and `trg`
    pvalue : float
        The p-value of `similarity`, if `nulls` is not None
    """

    methods = ('pearsonr', 'spearmanr')
    if metric not in methods:
        if not callable(metric):
            raise ValueError(f'Invalid `metric`: {metric}')
        else:
            if not isinstance(metric([1, 1], [1, 1]), float):
                raise ValueError('Provided callable `metric` must accept two '
                                 'inputs and return single value.')

    srcdata, trgdata = load_data(src), load_data(trg)

    mask = np.zeros(len(srcdata), dtype=bool)
    if ignore_zero:
        mask = np.logical_or(np.isclose(srcdata, 0), np.isclose(trgdata, 0))

    # drop NaNs
    nanmask = np.logical_or(np.isnan(srcdata), np.isnan(trgdata))
    if np.any(nanmask) and nan_policy == 'raise':
        raise ValueError('Inputs contain nan')
    mask = np.logical_and(np.logical_not(mask), np.logical_not(nanmask))
    srcdata, trgdata = srcdata[mask], trgdata[mask]

    if metric in methods:
        if metric == 'spearmanr':
            srcdata = sstats.rankdata(srcdata)
            trgdata = sstats.rankdata(trgdata)
        metric = partial(efficient_pearsonr, return_pval=False)

    if nulls is not None:
        n_perm = nulls.shape[-1]
        nulls = nulls[mask]
        return permtest_metric(srcdata, trgdata, metric, n_perm=n_perm,
                               nulls=nulls, nan_policy=nan_policy)

    return metric(srcdata, trgdata)


def permtest_metric(a, b, metric='pearsonr', n_perm=1000, seed=0, nulls=None,
                    nan_policy='propagate'):
    """
    Generates non-parameteric p-value of `a` and `b` for `metric`

    Calculates two-tailed p-value for hypothesis of whether samples `a` and `b`
    are related using permutation tests

    Parameters
    ----------
    a, b : (N,) array_like
        Sample observations. These arrays must have the same length
    metric : {'pearsonr', 'spearmanr', callable}, optional
        Type of similarity metric to use to compare `a` and `b`. If a callable
        function is provided it must accept two inputs and return a single
        value (the similarity metric). Default: 'pearsonr'
    n_perm : int, optional
        Number of permutations to assess. Unless `a` and `b` are very small
        this will approximate a randomization test via Monte Carlo simulations.
        Default: 1000
    seed : {int, np.random.RandomState instance, None}, optional
        Seed for random number generation. Set to None for pseudo-randomness.
        Default: 0
    nulls : (N, P) array_like, optional
        Null array used in place of shuffled `a` array to compute null
        distribution of correlations. Array must have the same length as `a`
        and `b`. Providing this will override the value supplied to `n_perm`.
        When not specified a standard permutation is used to shuffle `a`.
        Default: None
    nan_policy : {'propagate', 'raise', 'omit'}, optional
        Defines how to handle when inputs contain nan. 'propagate' returns nan,
        'raise' throws an error, 'omit' performs the calculations ignoring nan
        values. Default: 'propagate'

    Returns
    -------
    similarity : float
        Similarity metric
    pvalue : float
        Non-parametric p-value

    Notes
    -----
    The lowest p-value that can be returned by this function is equal to 1 /
    (`n_perm` + 1).
    """

    def nan_wrap(a, b, nan_policy='propagate'):
        nanmask = np.logical_or(np.isnan(a), np.isnan(b))
        if nan_policy == 'raise':
            if np.any(nanmask):
                raise ValueError('Input contains nan')
        elif nan_policy == 'omit':
            a, b = a[~nanmask], b[~nanmask]
        return metric(a, b)

    a, b, _ = _chk2_asarray(a, b, 0)
    rs = check_random_state(seed)

    if len(a) != len(b):
        raise ValueError('Provided arrays do not have same length')

    if a.size == 0 or b.size == 0:
        return np.nan, np.nan

    methods = ('pearsonr', 'spearmanr')
    if metric in methods:
        if metric == 'spearmanr':
            a, b = sstats.rankdata(a), sstats.rankdata(b)
        compfunc = partial(efficient_pearsonr, return_pval=False)
    else:
        compfunc = nan_wrap

    if nulls is not None:
        n_perm = nulls.shape[-1]

    # divide by one forces coercion to float if ndim = 0
    true_sim = compfunc(a, b, nan_policy=nan_policy) / 1
    abs_true = np.abs(true_sim)

    permutations = np.ones(true_sim.shape)
    for perm in range(n_perm):
        # permute `a` and determine whether correlations exceed original
        ap = a[rs.permutation(len(a))] if nulls is None else nulls[:, perm]
        permutations += np.abs(
            compfunc(ap, b, nan_policy=nan_policy)
        ) >= abs_true

    pvals = permutations / (n_perm + 1)  # + 1 in denom accounts for true_sim

    return true_sim, pvals


def efficient_pearsonr(a, b, ddof=1, nan_policy='propagate', return_pval=True):
    """
    Computes correlation of matching columns in `a` and `b`

    Parameters
    ----------
    a,b : array_like
        Sample observations. These arrays must have the same length and either
        an equivalent number of columns or be broadcastable
    ddof : int, optional
        Degrees of freedom correction in the calculation of the standard
        deviation. Default: 1
    nan_policy : {'propagate', 'raise', 'omit'}, optional
        Defines how to handle when input contains nan. 'propagate' returns nan,
        'raise' throws an error, 'omit' performs the calculations ignoring nan
        values. Default: 'propagate'

    Returns
    -------
    corr : float or numpy.ndarray
        Pearson's correlation coefficient between matching columns of inputs
    pval : float or numpy.ndarray
        Two-tailed p-values. Only returned if `return_pval` is True

    Notes
    -----
    If either input contains nan and nan_policy is set to 'omit', both arrays
    will be masked to omit the nan entries.
    """

    a, b, axis = _chk2_asarray(a, b, 0)
    if len(a) != len(b):
        raise ValueError('Provided arrays do not have same length')

    if a.size == 0 or b.size == 0:
        return np.nan, np.nan

    if nan_policy not in ('propagate', 'raise', 'omit'):
        raise ValueError(f'Value for nan_policy "{nan_policy}" not allowed')

    a, b = a.reshape(len(a), -1), b.reshape(len(b), -1)
    if (a.shape[1] != b.shape[1]):
        a, b = np.broadcast_arrays(a, b)

    mask = np.logical_or(np.isnan(a), np.isnan(b))
    if nan_policy == 'raise' and np.any(mask):
        raise ValueError('Input contains nan')
    elif nan_policy == 'omit':
        # avoid making copies of the data, if possible
        a = np.ma.masked_array(a, mask, copy=False, fill_value=np.nan)
        b = np.ma.masked_array(b, mask, copy=False, fill_value=np.nan)

    with np.errstate(invalid='ignore'):
        corr = (sstats.zscore(a, ddof=ddof, nan_policy=nan_policy)
                * sstats.zscore(b, ddof=ddof, nan_policy=nan_policy))

    sumfunc, n_obs = np.sum, len(a)
    if nan_policy == 'omit':
        corr = corr.filled(np.nan)
        sumfunc = np.nansum
        n_obs = np.squeeze(np.sum(np.logical_not(np.isnan(corr)), axis=0))

    corr = sumfunc(corr, axis=0) / (n_obs - 1)
    corr = np.squeeze(np.clip(corr, -1, 1)) / 1

    if return_pval:
        # taken from scipy.stats
        ab = (n_obs / 2) - 1
        prob = 2 * special.btdtr(ab, ab, 0.5 * (1 - np.abs(corr)))

        return corr, prob

    return corr
