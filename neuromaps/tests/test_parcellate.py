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


@pytest.mark.parametrize('hemi', ['L', 'R'])
@pytest.mark.parametrize('resampling_target', [None, 'data', 'parcellation'])
def test_Parcellater_single_hemi_array(hemi, resampling_target):
    """Test single-hemisphere data through the real fsaverage-3k path."""
    labels = np.ones(2562, dtype=int)
    labels[0] = 0
    atlas = construct_shape_gii(
        labels,
        intent='NIFTI_INTENT_LABEL',
        labels=['background', 'parcel'],
    )

    result = parcellate.Parcellater(
        atlas, 'fsaverage', resampling_target=resampling_target, hemi=hemi
    ).fit_transform(np.arange(2562), 'fsaverage', hemi=hemi)

    assert result == pytest.approx(1281.0)


@pytest.mark.xfail
def test_Parcellater():
    """Test Parcellater class."""
    assert False
