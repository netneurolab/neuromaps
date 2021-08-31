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

    >>> fslr_lh, fslr_rh = fslr
    >>> print(fslr_lh.agg_data().shape)
    (32492,)

It's just as easy to transform the data to a different space:

    >>> fsavg = transforms.mni152_to_fsaverage(neurosynth, '164k')
    >>> fsavg_lh, fsavg_rh = fsavg
    >>> print(fsavg_lh.agg_data().shape)
    (163842,)

Note that you can also transform between different resolutions within the
MNI152 coordinate system:

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
