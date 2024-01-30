# -*- coding: utf-8 -*-
"""For testing neuromaps.resampling functionality."""

import pytest

from neuromaps import resampling


@pytest.mark.xfail
def test__estimate_density():
    """Test estimating density."""
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_downsample_only():
    """Test downsampling a surface."""
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_transform_to_src():
    """Test transforming a surface to a volume."""
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_transform_to_trg():
    """Test transforming a surface to a volume."""
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_transform_to_alt():
    """Test transforming a surface to a volume."""
    assert False


@pytest.mark.xfail
def test_mni_transform():
    """Test transforming a surface to a volume."""
    assert False


def test__check_altspec():
    """Test checking alternative specifications."""
    spec = ('fsaverage', '10k')
    assert resampling._check_altspec(spec) == spec

    for spec in (None, ('fsaverage',), ('fsaverage', '100k')):
        with pytest.raises(ValueError):
            resampling._check_altspec(spec)


@pytest.mark.xfail
@pytest.mark.workbench
def test_resample_images():
    """Test resampling images."""
    assert False
