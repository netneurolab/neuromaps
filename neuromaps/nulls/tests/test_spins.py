# -*- coding: utf-8 -*-
"""
For testing neuromaps.nulls.spins functionality
"""

import numpy as np
import pytest

from neuromaps.nulls import spins


def test_load_spins():
    out = np.random.randint(1000, size=(100, 100), dtype='int32')
    assert out is spins.load_spins(out)
    assert np.allclose(out[:, :10], spins.load_spins(out, n_perm=10))


@pytest.mark.xfail
def test_get_parcel_centroids():
    assert False


@pytest.mark.xfail
def test__gen_rotation():
    assert False


@pytest.mark.xfail
def test_gen_spinsamples():
    assert False


@pytest.mark.xfail
def test_spin_parcels():
    assert False


@pytest.mark.xfail
def test_parcels_to_vertices():
    assert False


@pytest.mark.xfail
def test_vertices_to_parcels():
    assert False


@pytest.mark.xfail
def test_spin_data():
    assert False
