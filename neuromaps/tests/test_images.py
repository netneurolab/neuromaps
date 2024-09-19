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


@pytest.fixture(scope="session")
def dummy_img(request, tmp_path_factory):
    """Return a valid image file."""
    file_type = request.param["file_type"]
    return_type = request.param["return_type"]

    rng = np.random.default_rng()

    # create a valid image file
    if file_type == "nifti":
        data = rng.random((10, 10, 10))
        curr_img = nib.Nifti1Image(data, affine=np.eye(4))
        curr_path = tmp_path_factory.mktemp("nifti") \
            / "valid_nifti_file.nii.gz"
        nib.save(curr_img, str(curr_path))
    elif file_type == "gifti":
        data = rng.random((10, 10), dtype=np.float32)
        curr_img = nib.gifti.GiftiImage()
        gifti_data_array = nib.gifti.GiftiDataArray(data)
        curr_img.add_gifti_data_array(gifti_data_array)
        curr_path = tmp_path_factory.mktemp("gifti") \
            / "valid_gifti_file.gii"
        nib.save(curr_img, str(curr_path))
    else:
        raise ValueError(f"Invalid file type: {file_type}")

    # return the appropriate file type
    if return_type == "str":
        return str(curr_path)
    elif return_type == "path":
        return curr_path
    elif return_type == "object":
        return curr_img
    else:
        raise ValueError(f"Invalid return type: {return_type}")


@pytest.mark.parametrize(
    "dummy_img", [
        pytest.param(
            {"file_type": "nifti", "return_type": _}, 
            id=_
        ) for _ in ["str", "path", "object"]
    ], indirect=True
)
def test_load_nifti(dummy_img):
    """Test loading a NIfTI image."""
    res = images.load_nifti(dummy_img)
    assert isinstance(res, nib.Nifti1Image)


@pytest.mark.parametrize(
    "dummy_img", [
        pytest.param(
            {"file_type": "gifti", "return_type": _}, 
            id=_
        ) for _ in ["str", "path", "object"]
    ], indirect=True
)
def test_load_gifti(dummy_img):
    """Test loading a GIFTI image."""
    res = images.load_gifti(dummy_img)
    assert isinstance(res, nib.gifti.GiftiImage)


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
