# -*- coding: utf-8 -*-
"""
Fetching atlases and annotations
================================

This example demonstrates how to use :mod:`neuromaps.datasets` to fetch
atlases and annotations.
"""

###############################################################################
# Much of the functionality of the ``neuromaps`` toolbox relies on the
# atlases and atlas files provided with it. In many cases these atlases are
# fetched "behind-the-scenes" when you call functions that depend on them, but
# they can be accessed directly.
#
# There is a general purpose :func:`neuromaps.datasets.fetch_atlas`
# function that can fetch any of the atlases provided with ``neuromaps``:

from neuromaps import datasets

fslr = datasets.fetch_atlas(atlas='fslr', density='32k')
print(fslr.keys())

###############################################################################
# The values corresponding to the keys of the atlas dictionary are length-2
# lists containing filepaths to the downloaded data. All surface atlas files
# are provide in gifti format (whereas MNI files are in gzipped nifti format).
#
# You can load them directly with ``nibabel`` to confirm their validity:

import nibabel as nib
lsphere, rsphere = fslr['sphere']
lvert, ltri = nib.load(lsphere).agg_data()
print(lvert.shape, ltri.shape)

###############################################################################
# The other datasets that are provided with ``neuromaps`` are annotations
# (i.e., brain maps!). While we are slowly making more and more of these openly
# available, for now only a subset are accessible to the general public; these
# are returned by default via :func:`datasets.available_annotations`.

annotations = datasets.available_annotations()
print(f'Available annotations: {len(annotations)}')

###############################################################################
# The :func:`~.available_annotations` function accepts a number of keyword
# arguments that you can use to query specific datasets. For example, providing
# the `format='volume`' argument will return only those annotations that
# are, by default, a volumetric image:

volume_annotations = datasets.available_annotations(format='volume')
print(f'Available volumetric annotations: {len(volume_annotations)}')

###############################################################################
# There are a number of keyword arguments we can specify to reduce the scope of
# the annotations returned. Here, `source` specifies where the annotation came
# from (i.e., a dataset from a manuscript or a data repository or toolbox),
# `desc` refers to a brief description of the annotation, `space` clarifies
# which space the annotation is in, and `den` (specific to surface annotations)
# clarifies the density of the surface on which the annotation is defined:

annot = datasets.available_annotations(source='abagen', desc='genepc1',
                                       space='fsaverage', den='10k')
print(annot)

###############################################################################
# Annotations also have tags to help sort them into categories. You can see
# what tags can be used to query annotations with the :func:`~.available_tags`
# functions:

tags = datasets.available_tags()
print(tags)

###############################################################################
# Tags can be used as a keyword argument with :func:`~.available_annotations`.
# You can supply either a single tag or a list of tags. Note that supplying a
# list will only return those annotations that match ALL supplied tags:

fmri_annotations = datasets.available_annotations(tags='fMRI')
print(fmri_annotations)

###############################################################################
# Once we have an annotation that we want we can use the
# :func:`neuromaps.datasets.fetch_annotation` to actually download the
# files. This has a very similar signature to the
# :func:`~.available_annotations` function, accepting almost all the same
# keyword arguments to specify which annotations are desired.
#
# Here, we'll grab the first principal component of gene expression across the
# brain (from the Allen Human Brain Atlas):

abagen = datasets.fetch_annotation(source='abagen', desc='genepc1')
print(abagen)

###############################################################################
# Notice that the returned annotation ``abagen`` is a dictionary. We can subset
# the dictionary with the appropriate key or, if we know that our query is
# going to return only one annotation, also provide the `return_single=True`
# argument to the fetch call:

abagen = datasets.fetch_annotation(source='abagen', desc='genepc1',
                                   return_single=True)
print(abagen)

###############################################################################
# And that's it! This example provided a quick overview on how to fetch the
# various atlases and datasets provided with ``neuromaps``. For more
# information please refer to the :ref:`API reference <ref_datasets>`.
