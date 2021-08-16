# -*- coding: utf-8 -*-
"""
For testing neuromaps.transforms functionality
"""

import pytest

from neuromaps import transforms


@pytest.mark.xfail
def test__regfusion_project():
    assert False


@pytest.mark.xfail
def test__vol_to_surf():
    assert False


@pytest.mark.xfail
def test_mni152_to_civet():
    assert False


@pytest.mark.xfail
def test_mni152_to_fsaverage():
    assert False


@pytest.mark.xfail
def test_mni152_to_fslr():
    assert False


@pytest.mark.xfail
def test_mni152_to_mni152():
    assert False


def test__check_hemi():
    d, h = zip(*transforms._check_hemi('test', 'L'))
    assert d == ('test',) and h == ('L',)

    for d, h in (('test', None), ('test', 'invalid_hemi')):
        with pytest.raises(ValueError):
            transforms._check_hemi(d, h)


@pytest.mark.xfail
def test__surf_to_surf():
    assert False


@pytest.mark.xfail
def test_civet_to_fslr():
    assert False


@pytest.mark.xfail
def test_fslr_to_civet():
    assert False


@pytest.mark.xfail
def test_civet_to_fsaverage():
    assert False


@pytest.mark.xfail
def test_fsaverage_to_civet():
    assert False


@pytest.mark.xfail
def test_fslr_to_fsaverage():
    assert False


@pytest.mark.xfail
def test_fsaverage_to_fslr():
    assert False


@pytest.mark.xfail
def test_civet_to_civet():
    assert False


@pytest.mark.xfail
def test_fslr_to_fslr():
    assert False


@pytest.mark.xfail
def test_fsaverage_to_fsaverage():
    assert False
