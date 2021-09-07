# -*- coding: utf-8 -*-
"""
Workflow for making map comparisons
"""

from collections import defaultdict
from hashlib import sha256
import json

import nibabel as nib

from neuromaps import datasets, images, resampling, transforms, stats


def _get_null_func(null_method, space):
    from neuromaps import nulls

    if null_method == 'auto':
        return nulls.burt2020 if space == 'MNI152' else nulls.alexander_bloch
    else:
        try:
            return getattr(nulls, null_method)
        except AttributeError:
            raise ValueError(f'Invalid null_method value: {null_method}')


class Analysis:
    _hash_keys = (
        'annotation', 'space', 'hemi', 'parcellation', 'method', 'resampling',
        'alt_spec', 'metric', 'ignore_zero', 'null_method', 'n_perm',
        'nan_policy', 'seed', 'null_kwargs'
    )

    def __init__(self, annotation, space, target_annotations=None, hemi=None,
                 parcellation=None, method='linear',
                 resampling='downsample_only', alt_spec=None,
                 metric='pearsonr', ignore_zero=True, nulls=None,
                 null_method='auto', n_perm=1000, nan_policy='omit',
                 seed=1234, null_kwargs=None):
        self.annotation = annotation
        self.space = datasets.ALIAS.get(space, space)
        if self.space not in datasets.DENSITIES:
            raise ValueError(f'Invalid space: {space}')
        self.target_annotations = target_annotations
        self.parcellation = parcellation
        self.method = method
        self.resampling = resampling
        self.alt_spec = alt_spec
        self.metric = metric
        self.ignore_zero = ignore_zero
        self.n_perm = n_perm
        self.nan_policy = nan_policy
        self.seed = seed
        self.null_kwargs = null_kwargs if null_kwargs is not None else {}

        if self.space != 'MNI152':
            self.density, = transforms._estimate_density((self.annotation,))
            self.annotation, self.hemi = \
                zip(*transforms._check_hemi(annotation, hemi))
        else:
            aff = images.load_nifti(self.annotation).affine
            self.density, = set(nib.affines.voxel_sizes(aff))
            self.hemi = ('L', 'R') if hemi is None else hemi

        self.nulls = {(self.space, self.density): nulls}
        self.null_method = null_method
        self._fetch_annotations()
        self._stats = defaultdict(dict)

    def _generate_nulls(self, space, density, n_perm=None):
        if n_perm is not None:
            self.n_perm = n_perm

        nulls = self.nulls.get((space, density))
        if nulls is None and self.n_perm is not None and self.n_perm > 0:
            parcellation = None
            if self.parcellation is not None:
                parcellation = resampling.transform_to_trg(self.parcellation,
                                                           density, self.space,
                                                           space, self.hemi,
                                                           method='nearest')
            null_method = _get_null_func(self.null_method, space)
            nulls = null_method(self.annotation, atlas=space,
                                density=density, parcellation=parcellation,
                                n_perm=self.n_perm, seed=self.seed,
                                **self.null_kwargs)
            self.nulls[(space, density)] = nulls

        return nulls

    def _fetch_annotations(self):
        if self.target_annotations is None:
            targets = datasets.fetch_annotation(source='all', hemi=self.hemi)
        else:
            targets = {}
            volfmt = ('source', 'desc', 'space', 'res')
            surfmt = ('source', 'desc', 'space', 'den')
            for annotation in self.target_annotations:
                keys = volfmt if annotation[2] == 'MNI152' else surfmt
                annot = dict(zip(keys, annotation))
                targets[annotation] = \
                    datasets.fetch_annotation(**annot, hemi=self.hemi)

        self.target_annotations = targets

        return targets

    def _gen_hash(self):
        info = {key: getattr(self, key) for key in self._hash_keys}
        rep = json.dumps(info, default=str, sort_keys=True).encode()

        return sha256(rep).hexdigest()

    def _run_workflow(self):
        if self.nulls is None:
            self.nulls = self._generate_nulls(self.n_perm)

        hashkey = self._gen_hash()
        for key, annot in self.target_annotations.items():
            statistic = self._stats.get(hashkey, {}).get(key)
            if statistic is not None:
                yield key, statistic
                continue

            args = (self.annotation, annot, self.space, key[2])
            kwargs = dict(method=self.method, hemi=self.hemi,
                          resampling=self.resampling, alt_spec=self.alt_spec,
                          return_space=True)
            src, trg, space = resampling.resample_images(*args, **kwargs)
            nulls = self._generate_nulls(*space)
            statistic = stats.compare_images(src, trg, metric=self.metric,
                                             nulls=nulls,
                                             ignore_zero=self.ignore_zero,
                                             nan_policy=self.nan_policy)

            self._stats[hashkey][key] = statistic
            yield key, statistic

    def run(self):
        return list(self._run_workflow())
