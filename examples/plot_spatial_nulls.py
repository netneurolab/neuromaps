# -*- coding: utf-8 -*-
"""
Using spatial null models
=========================

This example demonstrates how to use spatial null models in
:mod:`neuromaps.nulls` to test the correlation between two brain
annotations.
"""

###############################################################################
# The brain—and most features derived from it—is spatially autocorrelated, and
# therefore when making comparisons between brain features we need to account
# for this spatial autocorrelation.
#
# Enter: spatial null models.
#
# Spatial null models need to be used whenever you're comparing brain maps. In
# order to demonstrate how use them in ``neuromaps`` we need two
# annotations to compare. We'll use the first principal component of cognitive
# terms from NeuroSynth (Yarkoni et al., 2011, Nat Methods) and the first
# principal component of gene expression across the brain (from the Allen Human
# Brain Atlas).
#
# Note that we pass `return_single=True` to
# :func:`neuromaps.datasets.fetch_annotation` so that the returned data are
# a list of filepaths rather than the default dictionary format. (This only
# works since we know that there is only one annotation matching our query; a
# dictionary will always be returned if multiple annotations match our query.)

from neuromaps import datasets
nsynth = datasets.fetch_annotation(source='neurosynth', return_single=True)
genepc = datasets.fetch_annotation(desc='genepc1', return_single=True)
print('Neurosynth: ', nsynth)
print('Gene PC1: ', genepc)

###############################################################################
# These annotations are in different spaces so we first need to resample them
# to the same space. Here, we'll choose to resample them to the 'fsaverage'
# surface with a '10k' resolution (approx 10k vertices per hemisphere). Note
# that the `genepc1` is already in this space so no resampling will be
# performed for those data. (We could alternatively specify 'transform_to_trg'
# for the `resampling` parameter and achieve the same outcome.)
#
# The data returned will always be pre-loaded nibabel image instances:

from neuromaps import resampling
nsynth, genepc = resampling.resample_images(src=nsynth, trg=genepc,
                                            src_space='MNI152',
                                            trg_space='fsaverage',
                                            resampling='transform_to_alt',
                                            alt_spec=('fsaverage', '10k'))
print(nsynth, genepc)

###############################################################################
# Once the images are resampled we can easily correlate them:

from neuromaps import stats
corr = stats.compare_images(nsynth, genepc)
print(f'Correlation: r = {corr:.02f}')

###############################################################################
# What if we want to assess the statistical significance of this correlation?
# In this case, we can use a null model from the :mod:`neuromaps.nulls` module.
#
# Here, we'll employ the null model proposed in Alexander-Bloch et al., 2018,
# *NeuroImage*. We provide one of the maps we're comparing, the space + density
# of the map, and the number of permutations we want to generate. The returned
# array will have two dimensions, where each row corresponds to a vertex and
# each column to a unique permutation.
#
# (Note that we need to pass the loaded data from the provided map to the null
# function so we use the :func:`neuromaps.images.load_data` utility.)

from neuromaps import images, nulls
nsynth_data = images.load_data(nsynth)
rotated = nulls.alexander_bloch(nsynth_data, atlas='fsaverage', density='10k',
                                n_perm=100, seed=1234)
print(rotated.shape)

###############################################################################
# We can supply the generated null array to the
# :func:`neuromaps.stats.compare_images` function and it will be used to
# generate a non-parameteric p-value. The function assumes that the array
# provided to the `nulls` parameter corresponds to the *first* dataset passed
# to the function (i.e., `nsynth`).
#
# Note that the correlation remains identical to that above but the p-value is
# now returned as well:

corr, pval = stats.compare_images(nsynth, genepc, nulls=rotated)
print(f'Correlation: r = {corr:.02f}, p = {pval:.04f}')

###############################################################################
# There are a number of different null functions that can be used to generate
# null maps; they have (nearly) identical function signatures, so refer to the
# :ref:`API reference <ref_nulls>` for more information.
