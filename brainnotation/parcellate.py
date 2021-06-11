# -*- coding: utf-8 -*-
"""
Functionality for parcellating data
"""

import nibabel as nib
from nilearn.input_data import NiftiLabelsMasker
import numpy as np

from brainnotation.images import construct_shape_gii, load_gifti
from brainnotation.resampling import resample_images
from brainnotation.transforms import _check_hemi
from brainnotation.nulls.spins import vertices_to_parcels, parcels_to_vertices


def _gifti_to_array(gifti):
    """ Converts tuple of `gifti` to numpy array
    """
    return np.hstack([load_gifti(img).agg_data() for img in gifti])


def _array_to_gifti(data):
    """ Converts numpy `array` to tuple of gifti images
    """
    return tuple(construct_shape_gii(arr) for arr in np.split(data, 2))


class Parcellater():
    def __init__(self, parcellation, space, resampling_target='data',
                 hemi=None):
        self.parcellation = parcellation
        self.space = space
        self.resampling_target = resampling_target
        self.hemi = hemi
        self._volumetric = self.space.lower() == 'mni152'

        if self.resampling_target == 'parcellation':
            self._resampling = 'transform_to_trg'
        else:
            self._resampling = 'transform_to_src'

        if not self._volumetric:
            self.parcellation, self.hemi = zip(
                *_check_hemi(self.parcellation, self.hemi)
            )

        if resampling_target not in ('parcellation', 'data', None):
            raise ValueError('Invalid value for `resampling_target`: '
                             f'{resampling_target}')

    def fit(self):
        if not self._volumetric:
            self.parcellation = tuple(
                load_gifti(img) for img in self.parcellation
            )
        self._fit = True
        return self

    def transform(self, data, space, hemi=None):
        self._check_fitted()

        if (self.resampling_target == 'data' and space.lower() == 'mni152' and
                not self._volumetric):
            raise ValueError('Cannot use resampling_target="data" when '
                             'provided parcellation is in surface space and '
                             'provided data are in MNI1512 space.')
        elif (self.resampling_target == 'parcellation' and self._volumetric
                and space.lower() != 'mni152'):
            raise ValueError('Cannot use resampling_target="parcellation" '
                             'when provided parcellation is in MNI152 space '
                             'and provided are in surface space.')

        if hemi is not None and hemi not in self.hemi:
            raise ValueError('Cannot parcellate data from {hemi} hemisphere '
                             'when parcellation was provided for incompatible '
                             'hemisphere: {self.hemi}')

        if isinstance(data, np.ndarray):
            data = _array_to_gifti(data)
        data, parc = resample_images(data, self.parcellation,
                                     space, self.space, hemi=hemi,
                                     resampling=self._resampling,
                                     method='nearest')

        if ((self.resampling_target == 'data'
             and space.lower() == 'mni152')
                or (self.resampling_target == 'parcellation'
                    and self._volumetric)):
            data = nib.concat_images([nib.squeeze_image(data)])
            parcellated = NiftiLabelsMasker(
                parc, resampling_target=self.resampling_target
            ).fit_transform(data)
        else:
            if not self._volumetric:
                for n, _ in enumerate(parc):
                    parc[n].labeltable.labels = \
                        self.parcellation[n].labeltable.labels
            data = _gifti_to_array(data)
            parcellated = vertices_to_parcels(data, parc)

        return parcellated

    def inverse_transform(self, data, hemi=None):
        if hemi is not None and hemi not in self.hemi:
            raise ValueError('Cannot parcellate data from {hemi} hemisphere '
                             'when parcellation was provided for incompatible '
                             'hemisphere: {self.hemi}')
        if not self._volumetric:
            verts = parcels_to_vertices(data, self.parcellation, self.drop)
            img = _array_to_gifti(verts)
        else:
            data = np.atleast_2d(data)
            img = NiftiLabelsMasker(self.parcellation).fit() \
                                                      .inverse_transform(data)
        return img

    def fit_transform(self, data, space, hemi=None):
        return self.fit().transform(data, space, hemi)

    def _check_fitted(self):
        if not hasattr(self, '_fit'):
            raise ValueError(f'It seems that {self.__class__.__name__} has '
                             'not been fit. You must call `.fit()` before '
                             'calling `.transform()`')
