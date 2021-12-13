# -*- coding: utf-8 -*-
"""
Workflow for making map comparisons
"""

from collections import defaultdict
from hashlib import sha256
import json

from neuromaps import datasets, transforms
from neuromaps.parcellate import Parcellater
from neuromaps.resampling import resample_images
from neuromaps.stats import compare_images


def _get_null_func(null_method, space):
    """ Gets null function for `null_method` and `space
    """
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
        """
        Creates workflow for comparing `annotation` to `target_annotations`

        Parameters
        ----------
        annotation : tuple-of-str or nib.GiftiImage or nib.Nifti1Image
            Brain map to be compared with `target_annotations`. Can be an array
            if `parcellation` is also provided.
        space : str
            Template space of input `annotation`
        target_annotations : list-of-tuple, optional
            Tuples should be of format (source, desc, space, den/res) as
            returned by e.g., :func:`neuromaps.datasets.available_annotations`.
            If not provided then all available annotations will be used.
            Default: None
        hemi : {'L', 'R'}, optional
            If `annotation` is a single surface hemisphere this specifies which
            hemisphere the data represent. Default: None
        parcellation : tuple-of-str or os.PathLike, optional
            Filepaths to parcellation image(s) that map data array `annotation`
            to template `space`. Default: None
        method : {'nearest', 'linear'}, optional
            Method for resampling. Should generally be kept at 'linear'; here
            largely for compatibility purposes. Default: 'linear'
        resampling : str, optional
            Name of resampling function to resample annotation images. Must be
            one of: 'downsample_only', 'transform_to_src', 'transform_to_trg',
            'transform_to_alt'. See Notes for more info. Default:
            'downsample_only'
        alt_spec : (2,) tuple-of-str, optional
            Where entries are (space, density) of desired target space. Only
            used if `resampling='transform_to_alt'`. Default: None
        metric : {'pearsonr', 'spearmanr', callable}, optional
            Type of similarity metric to use to compare annotation images.
            If a callable function is provided it must accept two inputs and
            return a single value (the similarity metric). Default: 'pearsonr'
        ignore_zero : bool, optional
            Whether to perform comparisons ignoring all zero values in
            annotation images. Default: True
        nulls : array_like, optional
            Null data for `annotation` to use in generating a non-parametric
            p-value. If not specified a parameteric p-value is generated.
            Default: None
        null_method : str, optional
            Name of null method to be used (e.g., `alexander_bloch`). If set
            to 'auto' then the null method will be chosen based on the input
            `annotation` format (alexander_bloch for surface data and burt2020
            for volumetric data). Default: 'auto'
        n_perm : int, optional
            Number of permutations to use when generating null maps. Default:
            1000
        nan_policy : {'propagate', 'raise', 'omit'}, optional
            Defines how to handle when input contains nan. 'propagate' returns
            nan, 'raise' throws an error, 'omit' performs the calculations
            ignoring nan values. Default: 'omit'
        seed : {int, np.random.RandomState instance, None}, optional
            Seed for random number generation when generating null maps. Set to
            None for pseudo-random generation. Default: 1234
        null_kwargs : dict, optional
            Keyword arguments passed directly to the underlying null method if
            `null_method` is not None. Default: None
        """

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

        img = parcellation if parcellation is not None else annotation
        if self.space != 'MNI152':
            self.density, = transforms._estimate_density((img,))
            _, self.hemi = zip(*transforms._check_hemi(img, hemi))
        else:
            self.density, = transforms._estimate_resolution((img,))
            self.hemi = ('L', 'R') if hemi is None else hemi

        self.nulls = {(self.space, self.density): nulls}
        self.null_method = null_method
        self._fetch_annotations()
        self._stats = defaultdict(dict)
        if self.parcellation is not None:
            self.parcellation = Parcellater(self.parcellation, self.space,
                                            resampling_target='data',
                                            hemi=self.hemi).fit()

    def _generate_nulls(self, space, density, n_perm=None):
        """ Generates null maps for specified `space` and `density`

        Null maps are cached for faster regeneration when called with identical
        inputs

        Parameters
        ----------
        space : str
            Template space of null maps to be generated
        density : str
            Density (or resolution) of null maps to be generated
        n_perm : int, optional
            Number of null maps to generate. Uses `self.n_perm` if None is
            supplied. Default: None

        Returns
        -------
        nulls : (V, N) np.ndarray
            Null maps where `V` is voxels/vertices and `N` is nulls
        """

        if n_perm is not None:
            self.n_perm = n_perm

        nulls = self.nulls.get((space, density))
        if nulls is None and self.n_perm is not None and self.n_perm > 0:
            parcellation = None
            if self.parcellation is not None:
                imgs = self.parcellation.parcellation
                parcellation = resample_images(imgs, density,
                                               self.space, space,
                                               hemi=self.hemi,
                                               resampling='transform_to_trg',
                                               method='nearest')[0]
            null_method = _get_null_func(self.null_method, space)
            nulls = null_method(self.annotation, atlas=space,
                                density=density, parcellation=parcellation,
                                n_perm=self.n_perm, seed=self.seed,
                                **self.null_kwargs)
            self.nulls[(space, density)] = nulls

        return nulls

    def _fetch_annotations(self):
        """ Populates `self.target_annotations` as dictionary object

        Returns
        -------
        targets : dict
            Where keys are tuples of (source, desc, space, den/res) and values
            are paths to image files
        """

        if self.target_annotations is None:
            targets = datasets.fetch_annotation(source='all', hemi=self.hemi)
        elif isinstance(self.target_annotations, dict):
            for k in self.target_annotations:
                if len(k) != 4:
                    raise ValueError('Provided `target_annotations` in '
                                     f'invalid format. Incorrect key: {k}')
            targets = self.target_annotations
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
        """
        Generates hash from current object state

        Hash is used for caching image similarity statistics to speed rerunning
        of workflow pipeline. Hash is based on keys defined in
        `Analysis._hash_keys`

        Returns
        -------
        sha : str
            Hash of current object values
        """

        info = {key: getattr(self, key) for key in self._hash_keys}
        rep = json.dumps(info, default=str, sort_keys=True).encode()

        return sha256(rep).hexdigest()

    def _run_workflow(self):
        """
        Runs workflow comparing `self.annotation` and `self.target_annotations`

        Yields
        ------
        annot : (4,) tuple-of-str
            Tuple defining compared annotation of format (source, desc, space,
            den/res)
        statistic : float or tuple-of-float
            Returns the image similarity statistic (`self.metric`). If
            `self.n_perm>0` then a tuple-of-float of (metric, p-value) is
            returned instead
        """

        if self.nulls is None:
            self.nulls = self._generate_nulls(self.n_perm)

        hashkey = self._gen_hash()
        for key, annot in self.target_annotations.items():
            statistic = self._stats.get(hashkey, {}).get(key)
            if statistic is not None:
                yield key, statistic
                continue

            if self.parcellation is None:
                args = (self.annotation, annot, self.space, key[2])
                kwargs = dict(method=self.method, hemi=self.hemi,
                              resampling=self.resampling,
                              alt_spec=self.alt_spec, return_space=True)
                src, trg, space = resample_images(*args, **kwargs)
                # should update this to work for any single hemisphere
                # target annotations
                if key[0] == 'hill2010':
                    src, _ = zip(*transforms._check_hemi(src, 'R'))
            else:
                src = self.annotation
                trg = self.parcellation.transform(annot, key[2])
                space = (self.space, self.parcellation._density)
            nulls = self._generate_nulls(*space)
            statistic = compare_images(src, trg, metric=self.metric,
                                       nulls=nulls,
                                       ignore_zero=self.ignore_zero,
                                       nan_policy=self.nan_policy)

            self._stats[hashkey][key] = statistic
            yield key, statistic

    def run(self):
        """
        Runs workflow comparing `self.annotation` to `self.target_annotations`

        Returns
        -------
        statistics : list-of-tuple
            Where entries of list are (annotation, statistic). The `annotation`
            entry is a tuple of (source, desc, space, den/res). If
            `self.n_perm` is not 0 then the `statistic` entry is itself a tuple
            of format (statistic, p-value)
        """

        return list(self._run_workflow())
