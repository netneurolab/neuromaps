# -*- coding: utf-8 -*-
"""For testing neuromaps.datasets.atlases functionality."""

import pytest

from neuromaps.datasets import atlases


@pytest.mark.parametrize('atlas, expected', [
    ('fslr', 'fsLR'), ('fsLR', 'fsLR'), ('fsavg', 'fsaverage'),
    ('fsaverage', 'fsaverage'), ('CIVET', 'civet'), ('civet', 'civet'),
    ('mni152', 'MNI152'), ('mni', 'MNI152'), ('MNI152', 'MNI152')
])
def test__sanitize_atlas(atlas, expected):
    """Test sanitizing atlas names."""
    assert atlases._sanitize_atlas(atlas) == expected


def test__sanitize_atlas_errors():
    """Test errors in _sanitize_atlas."""
    with pytest.raises(ValueError):
        atlases._sanitize_atlas('invalid')


@pytest.mark.xfail
def test__bunch_outputs():
    """Test bundling outputs."""
    assert False


@pytest.mark.xfail
def test__fetch_atlas():
    """Test fetching an atlas."""
    assert False


@pytest.mark.xfail
def test_fetch_civet():
    """Test fetching the CIVET atlas."""
    assert False


@pytest.mark.xfail
def test_fetch_fsaverage():
    """Test fetching the fsaverage atlas."""
    assert False


@pytest.mark.xfail
def test_fetch_mni152():
    """Test fetching the MNI152 atlas."""
    assert False


@pytest.mark.xfail
def test_fetch_regfusion():
    """Test fetching the regfusion atlas."""
    assert False


@pytest.mark.xfail
def test_fetch_atlas():
    """Test fetching an atlas."""
    assert False


@pytest.mark.xfail
def test_fetch_all_atlases():
    """Test fetching all atlases."""
    assert False


@pytest.mark.xfail
def test_get_atlas_dir():
    """Test getting the atlas directory."""
    assert False
