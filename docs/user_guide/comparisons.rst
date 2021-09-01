.. _usage_comparisons:

Comparing brain maps
====================

Resampling brain maps
---------------------

So you've got a new brain map and you want to compare it to some of the
annotations in the ``neuromaps`` repository. You know how to :ref:`fetch the
relevant annotations <usage_annotations>` and can :ref:`transform maps between
coordinate systems <usage_transformation>`. What now?

The :mod:`neuromaps.resampling` and :mod:`neuromaps.stats` modules contain
functions designed to streamline the process of making these comparisons.
First, let's say you have two annotations in different coordinate systems:

.. code-block::

    >>> from neuromaps.datasets import fetch_annotation
    >>> neurosynth = fetch_annotation(source='neurosynth')
    >>> abagen = fetch_annotation(source='abagen')

The `abagen` data are in the `fsaverage` system and the `neurosynth` data are
in the `MNI152` system. We can use :func:`neuromaps.resampling.resample_images`
to easily resample these images to a standard space.

.. code-block::

    >>> from neuromaps.resampling import resample_images
    >>> ns_res, aba_res = resample_images(src=neurosynth, trg=abagen,
    ...                                   src_space='MNI152', trg_space='fsaverage',
    ...                                   method='linear', resampling='downsample_only')


Only the first four parameters are required (i.e., ``src``, ``trg``,
``src_space``, and ``trg_space``). The other two parameters provided here
control how the resampling is done. The ``method='linear'`` specifies that we
should use linear interpolation when transforming the data between systems, as
described in :ref:`the transformations section <usage_transformations_method>`.
The ``resampling='downsample_only'`` parameter, on the other hand, controls
to what coordinate system the data are transformed.

There are four options for the ``resampling`` parameters:

  1. 'downsample_only',
  2. 'transform_to_src',
  3. 'transform_to_trg', and
  4. 'transform_to_alt'

The default ('downsample_only') specifies that the higher-resolution map will
be transformed to the space of the lower-resolution map. This ensures that we
are never artifically "creating" (i.e., upsampling) data that does not exist.

.. note::

    One caveat to the 'downsample_only' transformation: when one of the maps is
    in MNI152 space and the other is in a surface-based coordinate system the
    volumetric map is **always** transformed to the space of the surface-based
    map. In all other instances the higher-resolution map is transformed to the
    space of the lower-resolution map.

Note that when ``resampling='downsample_only'`` one of the inputs will always
remain unchanged. In the above example, the ``aba_res`` output will be
identical to the ``abagen`` input

.. code-block::

    >>> print(ns_res)
    (<nibabel.gifti.gifti.GiftiImage object at ...>, <nibabel.gifti.gifti.GiftiImage object at ...)
    >>> print(aba_res)
    ['/.../neuromaps-data/annotations/abagen/genepc1/fsaverage/source-abagen_desc-genepc1_space-fsaverage_den-10k_hemi-L_feature.func.gii', '/.../neuromaps-data/annotations/abagen/genepc1/fsaverage/source-abagen_desc-genepc1_space-fsaverage_den-10k_hemi-R_feature.func.gii']
    >>> print(abagen == aba_res)
    True

The 'transform_to_src' and 'transform_to_trg' options are relatively
straightforward: they specify that the function will transform the provided
data to the space of the 'src' or 'trg' dataset, respectively.

The 'transform_to_alt' parameter, on the other hand, works a bit differently.
It requires passing an additional argument to the ``resample_images`` function,
``alt_spec``:

.. code-block::

    >>> ns_fslr, aba_fslr = resample_images(src=neurosynth, trg=abagen,
    ...                                     src_space='MNI152', trg_space='fsaverage',
    ...                                     method='linear', resampling='transform_to_alt',
    ...                                     alt_spec=('fslr', '32k'))

The ``alt_spec`` parameter must be a tuple of format (system, density), and
specifies the target coordinate system and density to which both the ``src``
and ``trg`` datasets will be transformed. In the above example, both datasets
are transformed to the fsLR coordinate system and have an output density of 32k
vertices per hemisphere.

Statistical associations between maps
-------------------------------------

To assess the statistical relationship between two brain annotations in the
same coordinate system we can use :func:`neuromaps.stats.compare_images`:

.. code-block::

    >>> from neuromaps.stats import compare_images
    >>> corr = compare_images(ns_res, aba_res, metric='pearsonr')
    >>> print(f'r = {corr:.3f}')
    r = 0.339

We can use other image similarity metrics if we want by passing different
parameters to the ``metric`` argument. By default the only accepted string
arguments are ``'pearsonr'`` and ``'spearmanr``', but we can provide any
callable function that takes two vectors and returns a single value. For
example, we can calculate the cosine similarity of the images with:

.. code-block::

    >>> from scipy.spatial.distance import cosine
    >>> cossim = 1 - compare_images(ns_res, aba_res, metric=cosine)
    >>> print(f'cosine similarity = {cossim:.3f}')
    cosine similarity = 0.335

If we want to test the significance of these statistical associations we can
opt to use :ref:`spatial null models <usage_nulls>`.
