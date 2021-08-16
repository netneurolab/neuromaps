# -*- coding: utf-8 -*-
"""
For testing neuromaps.resampling functionality
"""

import pytest

from neuromaps import resampling


@pytest.mark.xfail
def test__estimate_density():
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_downsample_only():
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_transform_to_src():
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_transform_to_trg():
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_transform_to_alt():
    assert False


@pytest.mark.xfail
def test_mni_transform():
    assert False


def test__check_altspec():
    spec = ('fsaverage', '10k')
    assert resampling._check_altspec(spec) == spec

    for spec in (None, ('fsaverage',), ('fsaverage', '100k')):
        with pytest.raises(ValueError):
            resampling._check_altspec(spec)


@pytest.mark.xfail
@pytest.mark.workbench
def test_resample_images():
    assert False
