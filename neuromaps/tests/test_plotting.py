# -*- coding: utf-8 -*-
"""For testing neuromaps.plotting functionality."""

import pytest


@pytest.mark.xfail
def test_plot_surf_template():
    """Test plotting a surface template."""
    assert False


def test_register_cmap():
    """Test registering a colormap."""
    import matplotlib
    from neuromaps import plotting  # noqa: F401
    if "caret_blueorange" in matplotlib.colormaps:
        assert True
    else:
        assert False
