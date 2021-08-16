# -*- coding: utf-8 -*-
"""
Implementation of surrogate map generation as in Burt et al., 2018, Nat Neuro
"""

import warnings

import numpy as np
from scipy.optimize import least_squares
from scipy import sparse as ssp
from scipy.stats import boxcox


def _make_weight_matrix(x, d0):
    """
    Constructs weight matrix from distance matrix + autocorrelation estimate

    Parameters
    ----------
    x : array_like
        Distance matrix
    d0 : float
        Estimate of spatial scale of autocorrelation

    Returns
    -------
    W : numpy.ndarray
        Weight matrix
    """

    with np.errstate(over='ignore'):
        weight = np.exp(-x / d0) * np.logical_not(np.eye(len(x), dtype=bool))

    with np.errstate(invalid='ignore'):
        return weight / np.sum(weight, axis=1)


def estimate_rho_d0(x, y, rho=None, d0=None):
    """
    Uses a least-squares fit to estimate `rho` and `d0`

    Parameters
    ----------
    x : array_like
        Distance matrix
    y : array_like
        Dependent brain-imaging variable; all values must be positive in order
        for successful Box-Cox transformation
    rho : float, optional
        Initial guess for rho parameter. Default: 1.0
    d0 : float, optional
        Initial guess for d0 (spatial scale of autocorrelation) parameter.
        Default: 1.0

    Returns
    -------
    rho_hat : float
        Estimate of `rho` based on least-squares fit between `x` and `y`
    d0_hat : float
        Estimate of `d0` based on least-squares fit between `x` and `y`
    """

    def _estimate(parameters, x, y):
        rho, d0 = parameters
        y_hat = rho * (_make_weight_matrix(x, d0) @ y)
        return y - y_hat

    if rho is None:
        rho = 1.0
    if d0 is None:
        d0 = 1.0

    y, *_ = boxcox(y)
    y -= y.mean()

    return least_squares(_estimate, [rho, d0], args=(x, y), method='lm').x


def make_surrogate(x, y, rho=None, d0=None, seed=None, return_order=False,
                   return_params=False):
    """
    Generates surrogate map of `y`, retaining characteristic spatial features

    Parameters
    ----------
    x : array_like
        Distance matrix
    y : array_like
        Dependent brain-imaging variable; all values must be positive
    rho : float, optional
        Estimate for rho parameter. If not provided will be estimated from
        input data. Default: None
    d0 : float, optional
        Estimate for d0 parameter. If not provided will be estimated from input
        data. Default: None
    return_order : bool, optional
        Whether to return rank order of generated `surrogate` before values
        were replaced with `y`

    Returns
    -------
    surrogate : array_like
        Input `y` matrix, permuted according to surrogate map with similar
        spatial autocorrelation factor
    order : array_like
        Rank-order of `surrogate` before values were replaced with `y`
    """

    rs = np.random.default_rng(seed)

    if rho is None or d0 is None:
        rho, d0 = estimate_rho_d0(x, y, rho=rho, d0=d0)

    w = _make_weight_matrix(x, d0)
    u = rs.standard_normal(len(x))
    i = np.identity(len(x))
    surr = np.linalg.solve(i - rho * w, u)

    order = surr.argsort()
    surr[order] = np.sort(y)

    out = (surr,)

    if return_order:
        out += (order,)
    if return_params:
        out += ((rho, d0),)

    return out[0] if len(out) == 1 else out


def batch_surrogates(x, y, rho=None, d0=None, seed=None, n_surr=1000,
                     n_jobs=1):
    """
    Generates `n_surr` surrogates maps of `y` using Burt-2018 method

    Parameters
    ----------
    x : (N, N) array_like
        Distance matrix
    y : (N,) array_like
        Dependent brain-imaging variable; all values must be positive
    n_surr : int, optional
        Number of surrogates maps to generate. Default: 1000
    n_jobs : int, optional
        Number of processes to use while generating surrogate maps. Default: 1
    seed : {int, None}, optional
        Random seed for generating surrogates. Default: None

    Returns
    -------
    surrs : (N, `n_surr`)
        Generated surrogate maps
    """

    try:
        from joblib import Parallel, delayed
        joblib_avail = True
    except ImportError:
        if n_jobs != 1:
            warnings.warn('joblib not available; cannot parallelize')
        joblib_avail = False

    def _quick_surr(iw, ysort, seed=None):
        rs = np.random.default_rng(seed)
        u = rs.standard_normal(iw.shape[0])
        if ssp.issparse(iw):
            surr = ssp.linalg.spsolve(iw, u)
        else:
            surr = np.linalg.solve(iw, u)
        surr[surr.argsort()] = ysort

        return surr

    rs = np.random.default_rng(seed)
    seeds = rs.integers(np.iinfo(np.int32).max, size=n_surr)

    if rho is None or d0 is None:
        rho, d0 = estimate_rho_d0(x, y)
    iw = np.identity(len(x)) - rho * _make_weight_matrix(x, d0)
    zeros = np.isclose(iw, 0)
    if (zeros.sum() / iw.size) > 0.5:
        iw[np.isclose(iw, 0)] = 0
        iw = ssp.csr_matrix(iw)
    ysort = np.sort(y)

    if joblib_avail:
        surrs = Parallel(n_jobs=n_jobs)(
            delayed(_quick_surr)(iw, ysort, seed=seed) for seed in seeds
        )
    else:
        surrs = [_quick_surr(iw, ysort, seed=seed) for seed in seeds]

    return np.column_stack(surrs)
