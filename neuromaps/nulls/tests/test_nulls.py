# -*- coding: utf-8 -*-
"""
For testing neuromaps.nulls.nulls functionality
"""

import numpy as np
import pytest

from neuromaps.nulls import nulls


def test_naive_nonparametric():
    data = np.random.rand(50)
    perms = nulls.naive_nonparametric(data, n_perm=100)
    assert perms.shape == (50, 100)
    assert np.all(np.sort(perms, axis=0) == np.sort(data, axis=0)[:, None])

    resamples = nulls.naive_nonparametric(None, n_perm=100)
    assert resamples.shape == (20484, 100)
    assert np.all(np.sort(resamples, axis=0) == np.arange(20484)[:, None])


@pytest.mark.xfail
def test_alexander_bloch():
    assert False


@pytest.mark.xfail
def test_vasa():
    assert False


@pytest.mark.xfail
def test_hungarian():
    assert False


@pytest.mark.xfail
def test_baum():
    assert False


@pytest.mark.xfail
def test_cornblath():
    assert False


@pytest.mark.xfail
def test__get_distmat():
    assert False


@pytest.mark.xfail
def test__make_surrogates():
    assert False


@pytest.mark.xfail
def test_burt2018():
    assert False


@pytest.mark.xfail
def test_burt2020():
    assert False


@pytest.mark.xfail
def test_moran():
    assert False
