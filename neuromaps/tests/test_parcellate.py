# -*- coding: utf-8 -*-
"""For testing neuromaps.parcellate functionality."""

import numpy as np
import pytest

from neuromaps import parcellate
from neuromaps.images import construct_shape_gii


@pytest.mark.xfail
def test__gifti_to_array():
    """Test converting gifti to array."""
    assert False


@pytest.mark.parametrize('hemi, n_images, n_vertices', [
    (None, 2, (321, 321)),
    ('L', 1, (642,)),
    ('R', 1, (642,)),
])
def test__array_to_gifti(hemi, n_images, n_vertices):
    """Test converting array to gifti."""
    images = parcellate._array_to_gifti(np.arange(642), hemi=hemi)

    assert len(images) == n_images
    assert tuple(len(image.agg_data()) for image in images) == n_vertices


def test_Parcellater_single_hemi_array(monkeypatch):
    """Test parcellating single-hemisphere array data."""
    labels = np.ones(642, dtype=int)
    labels[0] = 0
    atlas = construct_shape_gii(
        labels,
        intent='NIFTI_INTENT_LABEL',
        labels=['background', 'parcel'],
    )

    def _resample_images(data, parc, *args, **kwargs):
        assert len(data) == 1
        assert len(data[0].agg_data()) == 642
        return data, parc

    monkeypatch.setattr(parcellate, 'resample_images', _resample_images)
    result = parcellate.Parcellater(
        atlas, 'fsaverage', resampling_target=None, hemi='L'
    ).fit_transform(np.arange(642), 'fsaverage', hemi='L')

    assert result == pytest.approx(321.0)


@pytest.mark.xfail
def test_Parcellater():
    """Test Parcellater class."""
    assert False
