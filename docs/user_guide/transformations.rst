.. _usage_transformations:

Transformations between coordinate systems
==========================================

Much of the "new" functionality in ``neuromaps`` is hosted in the
:mod:`neuromaps.transforms` module. The functionality in this module provides
easy-to-use interfaces for transforming brain annotations between all of the
:ref:`four standard coordinate systems <usage_atlases>` supported in
``neuromaps``.

The functions take on two formats (depending on whether the MNI152 volumetric
system is involved), which we discuss below.

.. _usage_transformations_volumetric:

Transforming from volumetric spaces
-----------------------------------

Curently ``neuromaps`` only supports transforming brain annotations *from*
MNI152 volumetric space to one of the other three surface-based coordinate
systems (though work in ongoing to integrate transformations in the other
direction!). This transformation is achieved through a process known as
"registration fusion" (Wu et al., 2018, *Hum Brain Mapping*). In order to
transform data from MNI152 space to another space you can use any of the
``neuromaps.transforms.mni152_to_XXX`` functions, where ``XXX`` is replaced
with the desired coordinate system.

For example, to transform data to the fsLR coordinate system:

.. code-block::

    >>> from neuromaps.datasets import fetch_annotation
    >>> from neuromaps import transforms
    >>> neurosynth = fetch_annotation(source='neurosynth')
    >>> fslr = transforms.mni152_to_fslr(neurosynth, '32k')

The returned ``fslr`` object is a tuple of ``nib.GiftiImage`` objects
corresponding to data from the (left, right) hemisphere. These data can be
accessed via the ``.agg_data()`` method on the image objects:

.. code-block::

    >>> fslr_lh, fslr_rh = fslr
    >>> print(fslr_lh.agg_data().shape)
    (32492,)

It's just as easy to transform the data to a different space:

.. code-block::

    >>> fsavg = transforms.mni152_to_fsaverage(neurosynth, '164k')
    >>> fsavg_lh, fsavg_rh = fsavg
    >>> print(fsavg_lh.agg_data().shape)
    (163842,)

Note that you can also transform between different resolutions within the
MNI152 coordinate system:

.. code-block::

    >>> import nibabel as nib
    >>> ns2mm = nib.load(neurosynth)
    >>> print(ns2mm.shape)
    (91, 109, 91)
    >>> ns3mm = transforms.mni152_to_mni152(neurosynth, '3mm')
    >>> print(ns3mm.shape)
    (91, 109, 91)

(This is frequently referred to as "resampling" and, indeed, we are really just
calling out to ``nilearn.image.resample_to_img``; we simply provide this
interface to ensure consistency!)

.. _usage_transformations_surface:

Transforming to/from surface spaces
-----------------------------------

Transforming between surface-based coordinate systems works bidirectionally.
That is, data in each surface system can be transformed to and from every other
surface system. Here, the transformation functions take the form of
``neuromaps.transforms.XXX_to_YYY`` where ``XXX`` is the source system and
``YYY`` is the target system.

For example, to transform data from the fsaverage to the fsLR coordinate
system:

.. code-block::

    >>> abagen = fetch_annotation(source='abagen')
    >>> fslr = transforms.fsaverage_to_fslr(abagen, '32k')

As with the volumetric-to-surface transformation, the returned object is a
tuple of ``nib.GiftiImage`` objects corresponding to data from the
(left, right) hemisphere.

.. code-block::

    >>> fslr_lh, fslr_rh = fslr
    >>> print(fslr_lh.agg_data().shape)
    (32492,)

Note that, by default, all of the transformation functions assume the provided
tuple contains data in the format (left hemisphere, right hemisphere) and
performs linear interpolation when resampling data to the new coordinate
system. However, the surface functions in :mod:`neuromaps.transforms` accept
two optional keyword parameters that can modify these defaults!

.. _usage_transformations_hemi:

Single-hemisphere data
^^^^^^^^^^^^^^^^^^^^^^

What happens when you want to transform annotations for which only one
hemisphere contains data? You can use the ``hemi`` keyword parameter to let
the transformation functions know:

.. code-block::

    >>> abagen_lh = abagen[0]
    >>> fslr = transforms.fsaverage_to_fslr(abagen_lh, '32k', hemi='L')

Note that the returned object is still a tuple—it just simply has one entry
instead of two!

.. code-block::

    >>> fslr_lh, = fslr
    >>> print(fslr_lh.agg_data().shape)
    (32492,)

The ``hemi`` parameter accepts values `'L'` and `'R'` for the left and right
hemispheres, respectively.

You can also use the ``hemi`` parameter if you want to provide bilateral data
that is not in the (left, right) hemisphere format:

.. code-block::

    >>> abagen_reverse = (abagen[1], abagen[0])
    >>> fslr_rh, fslr_lh = transforms.fsaverage_to_fslr(abagen_reverse, '32k', hemi=('R', 'L'))

.. _usage_transformations_method:

Nearest-neighbors interpolation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default the transformation functions in :mod:`neuromaps.transforms` use
linear interpolation when resampling data; however, this is not ideal if
the data that are being used are integer-valued (e.g., if the data represent a
parcellation)—or if you would simply prefer not to use linear interpolation! In
either case you can pass the ``method`` keyword parameter to the transform
functions and specify that you would prefer ``'nearest'`` neighbors
interpolation instead:

.. code-block::

    >>> fslr_nearest = transforms.fsaverage_to_fslr(abagen, '32k', method='nearest')

Note that the only accepted values for ``method`` are ``'linear'`` and
``'nearest'``.
