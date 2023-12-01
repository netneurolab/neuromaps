# -*- coding: utf-8 -*-
"""For testing neuromaps.transforms functionality."""

import pytest

from neuromaps import transforms


@pytest.mark.xfail
def test__regfusion_project():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test__vol_to_surf():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test_mni152_to_civet():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test_mni152_to_fsaverage():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test_mni152_to_fslr():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test_mni152_to_mni152():
    """Test projecting a volume to a surface."""
    assert False


def test__check_hemi():
    """Test checking the hemisphere."""
    d, h = zip(*transforms._check_hemi('test', 'L'))
    assert d == ('test',) and h == ('L',)

    for d, h in (('test', None), ('test', 'invalid_hemi')):
        with pytest.raises(ValueError):
            transforms._check_hemi(d, h)


@pytest.mark.xfail
def test__surf_to_surf():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_civet_to_fslr():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fslr_to_civet():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_civet_to_fsaverage():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fsaverage_to_civet():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fslr_to_fsaverage():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fsaverage_to_fslr():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_civet_to_civet():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fslr_to_fslr():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fsaverage_to_fsaverage():
    """Test projecting a surface to another surface."""
    assert False
