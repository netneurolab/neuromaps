# -*- coding: utf-8 -*-
"""
For testing neuromaps.stats functionality
"""

import numpy as np
import pytest

from neuromaps import stats


@pytest.mark.xfail
def test_compare_images():
    assert False


def test_permtest_metric():
    rs = np.random.default_rng(12345678)
    x, y = rs.random(size=(2, 100))
    r, p = stats.permtest_metric(x, y)
    assert np.allclose([r, p], [0.0345815411043023, 0.7192807192807192])

    r, p = stats.permtest_metric(np.c_[x, x[::-1]], np.c_[y, y])
    assert np.allclose(r, [0.0345815411043023, 0.03338608427980476])
    assert np.allclose(p, [0.7192807192807192, 0.7472527472527473])


@pytest.mark.parametrize('x, y, expected', [
    # basic one-dimensional input
    (range(5), range(5), (1.0, 0.0)),
    # broadcasting occurs regardless of input order
    (np.stack([range(5), range(5, 0, -1)], 1), range(5),
     ([1.0, -1.0], [0.0, 0.0])),
    (range(5), np.stack([range(5), range(5, 0, -1)], 1),
     ([1.0, -1.0], [0.0, 0.0])),
    # correlation between matching columns
    (np.stack([range(5), range(5, 0, -1)], 1),
     np.stack([range(5), range(5, 0, -1)], 1),
     ([1.0, 1.0], [0.0, 0.0]))
])
def test_efficient_pearsonr(x, y, expected):
    assert np.allclose(stats.efficient_pearsonr(x, y), expected)


def test_efficient_pearsonr_errors():
    with pytest.raises(ValueError):
        stats.efficient_pearsonr(range(4), range(5))

    assert all(np.isnan(a) for a in stats.efficient_pearsonr([], []))
