# -*- coding: utf-8 -*-
"""For testing neuromaps.images functionality."""

import nibabel as nib
import numpy as np
import pytest

from neuromaps import images


def test_construct_surf_gii():
    """Test constructing a surface GIFTI image."""
    vertices = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 1]])
    tris = np.array([[0, 1, 2]])
    surf = images.construct_surf_gii(vertices, tris)
    assert isinstance(surf, nib.GiftiImage)
    v, t = surf.agg_data()
    assert np.allclose(v, vertices) and np.allclose(t, tris)


@pytest.mark.xfail
def test_construct_shape_gii():
    """Test constructing a shape GIFTI image."""
    assert False


@pytest.mark.xfail
def test_fix_coordsys():
    """Test fixing the coordinate system of a GIFTI image."""
    assert False


@pytest.mark.xfail
def test_load_nifti():
    """Test loading a NIfTI image."""
    assert False


@pytest.mark.xfail
def test_load_gifti():
    """Test loading a GIFTI image."""
    assert False


@pytest.mark.xfail
def test_load_data():
    """Test loading a NIfTI or GIFTI image."""
    assert False


@pytest.mark.xfail
def test_obj_to_gifti():
    """Test converting an OBJ file to a GIFTI image."""
    assert False


@pytest.mark.xfail
def test_fssurf_to_gifti():
    """Test converting a FreeSurfer surface to a GIFTI image."""
    assert False


@pytest.mark.xfail
def test_fsmorph_to_gifti():
    """Test converting a FreeSurfer morphometry file to a GIFTI image."""
    assert False


@pytest.mark.xfail
def test_interp_surface():
    """Test interpolating a surface image."""
    assert False


@pytest.mark.xfail
def test_vertex_areas():
    """Test computing vertex areas for a surface image."""
    assert False


@pytest.mark.xfail
def test_average_surfaces():
    """Test averaging surface images."""
    assert False


@pytest.mark.xfail
def test_relabel_gifti():
    """Test relabeling a GIFTI image."""
    assert False


@pytest.mark.xfail
def test_annot_to_gifti():
    """Test converting a FreeSurfer annotation to a GIFTI image."""
    assert False


@pytest.mark.xfail
def test_dlabel_to_gifti():
    """Test converting a FreeSurfer dlabel file to a GIFTI image."""
    assert False


@pytest.mark.xfail
def test_minc_to_nifti():
    """Test converting a MINC file to a NIfTI image."""
    assert False
