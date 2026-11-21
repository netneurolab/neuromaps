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


@pytest.mark.parametrize('hemi, n_vertices', [(None, [5, 5]), ('L', [10])])
def test__array_to_gifti(hemi, n_vertices):
    """Test converting array to gifti."""
    images = parcellate._array_to_gifti(np.zeros(10), hemi=hemi)
    assert [len(img.agg_data()) for img in images] == n_vertices


@pytest.mark.parametrize('hemi', ['L', 'R'])
@pytest.mark.parametrize('resampling_target', ['data', 'parcellation'])
def test_Parcellater_single_hemi_array(hemi, resampling_target):
    """Test parcellating single-hemisphere array data."""
    # one fsaverage-3k parcel; vertex 0 is background
    labels = np.ones(2562, dtype=int)
    labels[0] = 0
    atlas = construct_shape_gii(labels, intent='NIFTI_INTENT_LABEL')
    parc = parcellate.Parcellater(atlas, 'fsaverage', hemi=hemi,
                                  resampling_target=resampling_target)
    result = parc.fit_transform(np.full(2562, 5.0), 'fsaverage', hemi=hemi)
    assert result == pytest.approx(5.0)


@pytest.mark.parametrize('hemi', ['L', 'R'])
def test_Parcellater_single_hemi_inverse_transform(hemi):
    """Test projecting parcellated data back to a single hemisphere."""
    # one fsaverage-3k parcel; vertex 0 is background
    labels = np.ones(2562, dtype=int)
    labels[0] = 0
    atlas = construct_shape_gii(labels, intent='NIFTI_INTENT_LABEL')
    parc = parcellate.Parcellater(atlas, 'fsaverage', hemi=hemi).fit()
    images = parc.inverse_transform(np.array([5.0]))
    assert len(images) == 1
    assert len(images[0].agg_data()) == 2562
    assert np.allclose(images[0].agg_data()[1:], 5.0)


@pytest.mark.xfail
def test_Parcellater():
    """Test Parcellater class."""
    assert False
