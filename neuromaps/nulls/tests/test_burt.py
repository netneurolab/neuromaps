# -*- coding: utf-8 -*-
"""
For testing neuromaps.nulls.burt functionality
"""

import numpy as np
import pytest

from neuromaps.nulls import burt


def test__make_weight_matrix():
    x0 = np.random.rand(100, 100)
    out = burt._make_weight_matrix(x0, 0.5)
    assert out.shape == x0.shape
    assert np.allclose(np.diag(out), 0)


@pytest.mark.xfail
def test_estimate_rho_d0():
    assert False


@pytest.mark.xfail
def test_make_surrogate():
    assert False


@pytest.mark.xfail
def test_batch_surrogates():
    assert False
