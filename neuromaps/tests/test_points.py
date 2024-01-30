# -*- coding: utf-8 -*-
"""For testing neuromaps.points functionality."""

import numpy as np
import pytest

from neuromaps import points


def test_point_in_triangle():
    """Test point in triangle."""
    triangle = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 1]])
    point = np.array([0, 0.5, 0.5])
    inside, pdist = points.point_in_triangle(point, triangle)
    assert inside and pdist == 0

    point = np.array([0.5, 0, 0])
    inside, pdist = points.point_in_triangle(point, triangle)
    assert inside and pdist == 0.5

    point = np.array([-0.5, -0.5, -0.5])
    inside, pdist = points.point_in_triangle(point, triangle)
    assert not inside and pdist == 0.5


@pytest.mark.xfail
def test_which_triangle():
    """Test which triangle."""
    assert False


@pytest.mark.xfail
def test_get_shared_triangles():
    """Test getting shared triangles."""
    assert False


@pytest.mark.xfail
def test_get_direct_edges():
    """Test getting direct edges."""
    assert False


@pytest.mark.xfail
def test_get_indirect_edges():
    """Test getting indirect edges."""
    assert False


@pytest.mark.xfail
def test_make_surf_graph():
    """Test making surface graph."""
    assert False


@pytest.mark.xfail
def test_get_surface_distance():
    """Test getting surface distance."""
    assert False
