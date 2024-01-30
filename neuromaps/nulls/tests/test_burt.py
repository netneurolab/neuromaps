# -*- coding: utf-8 -*-
"""For testing neuromaps.nulls.burt functionality."""

import numpy as np
import pytest

from neuromaps.nulls import burt


def test__make_weight_matrix():
    """Test making a weight matrix."""
    rng = np.random.default_rng()
    x0 = rng.random((100, 100))
    out = burt._make_weight_matrix(x0, 0.5)
    assert out.shape == x0.shape
    assert np.allclose(np.diag(out), 0)


@pytest.mark.xfail
def test_estimate_rho_d0():
    """Test estimating rho and d0."""
    assert False


@pytest.mark.xfail
def test_make_surrogate():
    """Test making a surrogate."""
    assert False


@pytest.mark.xfail
def test_batch_surrogates():
    """Test batching surrogates."""
    assert False
