# -*- coding: utf-8 -*-
"""
For testing neuromaps.datasets.atlases functionality
"""

import pytest

from neuromaps.datasets import atlases


@pytest.mark.parametrize('atlas, expected', [
    ('fslr', 'fsLR'), ('fsLR', 'fsLR'), ('fsavg', 'fsaverage'),
    ('fsaverage', 'fsaverage'), ('CIVET', 'civet'), ('civet', 'civet'),
    ('mni152', 'MNI152'), ('mni', 'MNI152'), ('MNI152', 'MNI152')
])
def test__sanitize_atlas(atlas, expected):
    assert atlases._sanitize_atlas(atlas) == expected


def test__sanitize_atlas_errors():
    with pytest.raises(ValueError):
        atlases._sanitize_atlas('invalid')


@pytest.mark.xfail
def test__bunch_outputs():
    assert False


@pytest.mark.xfail
def test__fetch_atlas():
    assert False


@pytest.mark.xfail
def test_fetch_civet():
    assert False


@pytest.mark.xfail
def test_fetch_fsaverage():
    assert False


@pytest.mark.xfail
def test_fetch_mni152():
    assert False


@pytest.mark.xfail
def test_fetch_regfusion():
    assert False


@pytest.mark.xfail
def test_fetch_atlas():
    assert False


@pytest.mark.xfail
def test_fetch_all_atlases():
    assert False


@pytest.mark.xfail
def test_get_atlas_dir():
    assert False
