# -*- coding: utf-8 -*-
"""
For testing neuromaps.images functionality
"""

import nibabel as nib
import numpy as np
import pytest

from neuromaps import images


def test_construct_surf_gii():
    vertices = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 1]])
    tris = np.array([[0, 1, 2]])
    surf = images.construct_surf_gii(vertices, tris)
    assert isinstance(surf, nib.GiftiImage)
    v, t = surf.agg_data()
    assert np.allclose(v, vertices) and np.allclose(t, tris)


@pytest.mark.xfail
def test_construct_shape_gii():
    assert False


@pytest.mark.xfail
def test_fix_coordsys():
    assert False


@pytest.mark.xfail
def test_load_nifti():
    assert False


@pytest.mark.xfail
def test_load_gifti():
    assert False


@pytest.mark.xfail
def test_load_data():
    assert False


@pytest.mark.xfail
def test_obj_to_gifti():
    assert False


@pytest.mark.xfail
def test_fssurf_to_gifti():
    assert False


@pytest.mark.xfail
def test_fsmorph_to_gifti():
    assert False


@pytest.mark.xfail
def test_interp_surface():
    assert False


@pytest.mark.xfail
def test_vertex_areas():
    assert False


@pytest.mark.xfail
def test_average_surfaces():
    assert False


@pytest.mark.xfail
def test_relabel_gifti():
    assert False


@pytest.mark.xfail
def test_annot_to_gifti():
    assert False


@pytest.mark.xfail
def test_dlabel_to_gifti():
    assert False


@pytest.mark.xfail
def test_minc_to_nifti():
    assert False
