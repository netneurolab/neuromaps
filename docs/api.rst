.. _api_ref:

.. currentmodule:: brainnotation

Reference API
=============

.. contents:: **List of modules**
   :local:

.. _ref_datasets:

:mod:`brainnotation.datasets` - Dataset fetchers
------------------------------------------------
.. automodule:: brainnotation.datasets
   :no-members:
   :no-inherited-members:

.. currentmodule:: brainnotation.datasets

.. autosummary::
   :template: function.rst
   :toctree: generated/

   brainnotation.datasets.fetch_atlas
   brainnotation.datasets.fetch_civet
   brainnotation.datasets.fetch_fsaverage
   brainnotation.datasets.fetch_fslr
   brainnotation.datasets.fetch_mni152
   brainnotation.datasets.fetch_regfusion
   brainnotation.datasets.fetch_all_atlases

   brainnotation.datasets.available_annotations
   brainnotation.datasets.available_tags
   brainnotation.datasets.fetch_annotation

   brainnotation.datasets.get_atlas_dir

.. _ref_images:

:mod:`brainnotation.images` - Image and surface handling
--------------------------------------------------------
.. automodule:: brainnotation.images
   :no-members:
   :no-inherited-members:

.. currentmodule:: brainnotation.images

.. autosummary::
   :template: function.rst
   :toctree: generated/


   brainnotation.images.load_gifti
   brainnotation.images.load_nifti

   brainnotation.images.average_surfaces
   brainnotation.images.interp_surface
   brainnotation.images.vertex_areas

   brainnotation.images.relabel_gifti
   brainnotation.images.annot_to_gifti
   brainnotation.images.dlabel_to_gifti
   brainnotation.images.obj_to_gifti
   brainnotation.images.fssurf_to_gifti
   brainnotation.images.fsmorph_to_gifti

.. _ref_nulls:

:mod:`brainnotation.nulls` - Null models
----------------------------------------
.. automodule:: brainnotation.nulls
   :no-members:
   :no-inherited-members:

.. currentmodule:: brainnotation.nulls

.. autosummary::
   :template: function.rst
   :toctree: generated/

   brainnotation.nulls.naive_nonparametric
   brainnotation.nulls.alexander_bloch
   brainnotation.nulls.vazquez_rodriguez
   brainnotation.nulls.vasa
   brainnotation.nulls.hungarian
   brainnotation.nulls.baum
   brainnotation.nulls.cornblath

   brainnotation.nulls.burt2018
   brainnotation.nulls.burt2020
   brainnotation.nulls.moran

.. _ref_parcellating:

:mod:`brainnotation.parcellate` - Parcellation utilities
--------------------------------------------------------
.. automodule:: brainnotation.parcellate
   :no-members:
   :no-inherited-members:

.. currentmodule:: brainnotation.parcellate

.. autosummary::
   :template: class.rst
   :toctree: generated/

   brainnotation.parcellate.Parcellater

.. _ref_plotting:

:mod:`brainnotation.plotting` - Plotting functions
--------------------------------------------------
.. automodule:: brainnotation.plotting
   :no-members:
   :no-inherited-members:

.. currentmodule:: brainnotation.plotting

.. autosummary::
   :template: function.rst
   :toctree: generated/

   brainnotation.plotting.plot_surf_template

.. _ref_resampling:

:mod:`brainnotation.resampling` - Resampling workflows
------------------------------------------------------
.. automodule:: brainnotation.resampling
    :no-members:
    :no-inherited-members:

.. currentmodule:: brainnotation.resampling

.. autosummary::
    :template: function.rst
    :toctree: generated/

    brainnotation.resampling.resample_images


.. _ref_transforms:

:mod:`brainnotation.transforms` - Transformations between spaces
----------------------------------------------------------------
.. automodule:: brainnotation.transforms
   :no-members:
   :no-inherited-members:

.. currentmodule:: brainnotation.transforms

.. autosummary::
   :template: function.rst
   :toctree: generated/

   brainnotation.transforms.mni152_to_civet
   brainnotation.transforms.mni152_to_fsaverage
   brainnotation.transforms.mni152_to_fslr
   brainnotation.transforms.mni152_to_mni152

   brainnotation.transforms.civet_to_fslr
   brainnotation.transforms.fslr_to_civet
   brainnotation.transforms.civet_to_fsaverage
   brainnotation.transforms.fsaverage_to_civet
   brainnotation.transforms.civet_to_civet
   brainnotation.transforms.fslr_to_fsaverage
   brainnotation.transforms.fsaverage_to_fslr
   brainnotation.transforms.fslr_to_fslr
   brainnotation.transforms.fsaverage_to_fsaverage

.. _ref_stats:

:mod:`brainnotation.stats` - Statistical functions
--------------------------------------------------
.. automodule:: brainnotation.stats
   :no-members:
   :no-inherited-members:

.. currentmodule:: brainnotation.stats

.. autosummary::
   :template: function.rst
   :toctree: generated/

   brainnotation.stats.correlate_images
   brainnotation.stats.efficient_pearsonr
   brainnotation.stats.permtest_pearsonr
