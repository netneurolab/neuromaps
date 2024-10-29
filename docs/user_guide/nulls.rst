.. _usage_nulls:

Spatial nulls for significance testing
======================================

In the :ref:`last section <usage_comparisons>` we showed how to resample and
statistically compare two brain annotations. This process gave us a correlation
estimate (or other image similarity metric) but no means by which to test the
significance of the association between the tested maps. Enter: the
:mod:`neuromaps.nulls` module.

This module provides access to a variety of null models that can be used to
generate "null" brain maps that retain aspects of the spatial autocorrelation
of the original brain maps. 

For a review of these models, please refer to
`Markello & Misic, 2021, NeuroImage <https://doi.org/10.1016/j.neuroimage.2021.118052>`_.
We also recommend watching  `this recorded session <https://www.youtube.com/watch?v=6DjpNddINZ8>`_
from the OHBM 2024 Educational Course if you are new to this topic.

There are four available null models that can be used with voxel- and
vertex-wise data and eight null models that can be used with parcellated data.
Refer to the :mod:`neuromaps.nulls` API for the complete list of null models.

.. _usage_nulls_surface:

Nulls with surface-based data
-----------------------------

.. _usage_nulls_nonparc:

Nulls with non-parcellated data
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All of the null model functions in ``neuromaps`` have (more-or-less) identical
interfaces. They accept (1) a data array or tuple-of-images, (2) the coordinate
system + density of the provided data, (3) the number of desired nulls
(i.e., permutations), and (4) a random seed for reproducibility. The functions
will yield a two-dimensional array of shape (vertices, nulls):

.. code-block::

    >>> from neuromaps import datasets, images, nulls, resampling
    >>> neurosynth = datasets.fetch_annotation(source='neurosynth')
    >>> abagen = datasets.fetch_annotation(source='abagen')
    >>> neurosynth, abagen = resampling.resample_images(neurosynth, abagen, 'MNI152', 'fsaverage')
    >>> rotated = nulls.alexander_bloch(neurosynth, atlas='fsaverage', density='10k',
    ...                                 n_perm=100, seed=1234)
    >>> print(rotated.shape)
    (20484, 100)

Once we've generated the null maps we can pass them directly to the optional
``nulls`` argument of :func:`neuromaps.stats.compare_images`


.. code-block::

    >>> from neuromaps import stats
    >>> corr, pval = stats.compare_images(neurosynth, abagen, nulls=rotated)
    >>> print(f'r = {corr:.3f}, p = {pval:.3f}')
    r = 0.339, p = 0.178

.. important::

    The null array provided to the ``nulls`` argument must be for the data
    passed as the first positional argument of the function! In the above
    example, the ``rotated`` array corresponds to null maps for ``neurosynth``.
    If we called the function like ``stats.compare_images(abagen, neurosynth)``
    then we would have had to generate our ``rotated`` array for the ``abagen``
    data instead. The function has no way of checking this so you must be very
    careful when providing null arrays!

Now, our call to ``compare_images()`` returns both a correlation and a p-value.
Note that the p-values are bounded based on the requested number of
permutations. That is, if you provide an array to ``nulls`` the smallest
p-value that can be returned is ``(1 / (1 + nulls.shape[1]))``.

.. _usage_nulls_parc:

Nulls with parcellated data
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The null model functions in ``neuromaps`` can also handle parcellated data, and
do so by accepting an additional optional keyword parameter: ``parcellation``.
If provided, the null functions assume this is a tuple-of-images (left, right
hemisphere, as usual) that is in the same space as the provided ``data``.

Generally you will already have pre-parcellated data, but for the purposes of
demonstration we we will fetch a surface parcellation (for the 10k `fsaverage`
system) using ``nilearn``:

.. code-block::

    >>> from nilearn.datasets import fetch_atlas_surf_destrieux
    >>> destrieux = fetch_atlas_surf_destrieux()
    >>> print(sorted(destrieux))
    ['description', 'labels', 'map_left', 'map_right']
    >>> print(len(destrieux['map_left']), len(destrieux['map_right']))
    10242 10242
    >>> print(len(destrieux['labels']))
    76

Unfortunately the Destrieux atlas provided here is designed such that left
and right hemispheres have identical label values. The functions in
``neuromaps`` that handle parcellated data always assume that the labels IDs
are ascending across hemispheres. Moreover, the ``map_left`` and ``map_right``
values are simple numpy arrays and ``neuromaps`` prefers to work with GIFTI
images. We can convert the arrays to GIFTI label images and then relabel them
so that the labels are consecutive across hemispheres:

.. code-block::

    >>> labels = [label.decode() for label in destrieux['labels']]
    >>> parc_left = images.construct_shape_gii(destrieux['map_left'], labels=labels,
    ...                                        intent='NIFTI_INTENT_LABEL')
    >>> parc_right = images.construct_shape_gii(destrieux['map_right'], labels=labels,
    ...                                         intent='NIFTI_INTENT_LABEL')
    >>> parcellation = images.relabel_gifti((parc_left, parc_right), background=['Medial_wall'])
    >>> print(parcellation)
    (<nibabel.gifti.gifti.GiftiImage object at ...>, <nibabel.gifti.gifti.GiftiImage object at ...>)

Note that we set ``background=['Medial_wall']`` in our call to
:func:`~.images.relabel_gifti`. This is because, by default, the medial wall
has a label of 42 and we want it to be set to 0. (The ``neuromaps`` functions
assume that the 0 label is the background, and it is omitted from most
calculations.)

We can use these images to parcellate our data with an instance of the
:class:`neuromaps.parcellate.Parcellater` class:

.. code-block::

    >>> from neuromaps import parcellate
    >>> destrieux = parcellate.Parcellater(parcellation, 'fsaverage').fit()
    >>> neurosynth_parc = destrieux.transform(neurosynth, 'fsaverage')
    >>> abagen_parc = destrieux.transform(abagen, 'fsaverage')
    >>> print(neurosynth_parc.shape, abagen_parc.shape)
    (148,) (148,)

Now that we've got our parcellated arrays we can generate our null maps. We
use the same call as :ref:`above <usage_nulls_nonparc>` but provide the
additional ``parcellation`` parameter:

.. code-block::

    >>> rotated = nulls.alexander_bloch(neurosynth_parc, atlas='fsaverage', density='10k',
    ...                                 n_perm=100, seed=1234, parcellation=parcellation)
    >>> print(rotated.shape)
    (148, 100)

We can pass the generated array to the ``nulls`` argument of
:func:`~.stats.compare_images` as before:

.. code-block::

    >>> corr, pval = stats.compare_images(neurosynth_parc, abagen_parc, nulls=rotated)
    >>> print(f'r = {corr:.3f}, p = {pval:.3f}')
    r = 0.416, p = 0.376

The correlation has changed (because we parcellated the data!), but remains
non-significant.

.. _usage_nulls_volumetric:

Nulls for volumetric data
-------------------------

.. warning::
   Nulls for high-resolution volumetric data (especially at 1mm or 2mm resolution) can
   be **extremely** demanding (days & hundreds of GBs). This is an inherent limitation
   of the original model that currently has no immediate workaround!

The majority of spatial nulls work best with data represented in one of the
surface-based coordinate systems. If you are working with data that are
represented in the MNI152 system you must use one of the following three null
models:

    1. :func:`neuromaps.nulls.burt2018`,
    2. :func:`neuromaps.nulls.burt2020`, or
    3. :func:`neuromaps.nulls.moran`

Whereas the other available null models assume that the provided data are
represented on a cortical surface, these models are more flexible. *However*,
they all depend on calculating and storing a distance matrix of the provided
images in memory, and as such will be **very computationally intensive** for
volumetric images.

You would call the functions in the same manner as above:

.. code-block::

    >>> neurosynth_mni152 = datasets.fetch_annotation(source='neurosynth')
    >>> nulls = nulls.burt2020(neurosynth_mni152, atlas='MNI152', density='2mm',
    ...                        n_perm=100, seed=1234)
    >>> print(nulls.shape)
    (224705, 100)


When working with volumetric data, please note some important computational
considerations. While the function supports both voxelwise and parcellated analyses,
processing high-resolution volumetric data (especially at 1mm or 2mm resolution) can
be **extremely** demanding. The calculations for voxelwise data can take several days
to complete even on high-performance computing nodes, and may require hundreds of GBs
of temporary storage space. This is an inherent limitation of the original model that
currently has no immediate workaround (see `BrainSMASH <https://github.com/murraylab/brainsmash>`_).
We welcome any suggestions for improving this method's computational efficiency and
performance.

To make your analysis more tractable, we recommend you consider using parcellated
data instead of voxelwise analysis. Parcellation dramatically reduces both computation
time and storage requirements.

For voxelwise input, if possible it is recommended that you mask your data
(i.e., with a gray matter mask) before generating nulls using this procedure. To use
parcellation images for volumetric data, simply pass the volumetric parcellation image
to the ``parcellation`` keyword argument and the function will take care of the rest.
