.. _api_ref:

.. currentmodule:: neuromaps

Reference API
=============

.. contents:: **List of modules**
   :local:

.. _ref_datasets:

:mod:`neuromaps.datasets` - Dataset fetchers
--------------------------------------------
.. automodule:: neuromaps.datasets
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.datasets

.. autosummary::
   :template: function.rst
   :toctree: generated/

   neuromaps.datasets.fetch_atlas
   neuromaps.datasets.fetch_civet
   neuromaps.datasets.fetch_fsaverage
   neuromaps.datasets.fetch_fslr
   neuromaps.datasets.fetch_mni152
   neuromaps.datasets.fetch_regfusion
   neuromaps.datasets.fetch_all_atlases

   neuromaps.datasets.available_annotations
   neuromaps.datasets.available_tags
   neuromaps.datasets.fetch_annotation

   neuromaps.datasets.get_atlas_dir

   neuromaps.datasets.upload_annotation

.. _ref_images:

:mod:`neuromaps.images` - Image and surface handling
----------------------------------------------------
.. automodule:: neuromaps.images
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.images

.. autosummary::
   :template: function.rst
   :toctree: generated/


   neuromaps.images.load_gifti
   neuromaps.images.load_nifti

   neuromaps.images.average_surfaces
   neuromaps.images.interp_surface
   neuromaps.images.vertex_areas

   neuromaps.images.relabel_gifti
   neuromaps.images.annot_to_gifti
   neuromaps.images.dlabel_to_gifti
   neuromaps.images.obj_to_gifti
   neuromaps.images.fssurf_to_gifti
   neuromaps.images.fsmorph_to_gifti

.. _ref_nulls:

:mod:`neuromaps.nulls` - Null models
------------------------------------
.. automodule:: neuromaps.nulls
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.nulls

.. autosummary::
   :template: function.rst
   :toctree: generated/

   neuromaps.nulls.alexander_bloch
   neuromaps.nulls.vazquez_rodriguez
   neuromaps.nulls.vasa
   neuromaps.nulls.hungarian
   neuromaps.nulls.baum
   neuromaps.nulls.cornblath

   neuromaps.nulls.burt2018
   neuromaps.nulls.burt2020
   neuromaps.nulls.moran

.. _ref_parcellating:

:mod:`neuromaps.parcellate` - Parcellation utilities
----------------------------------------------------
.. automodule:: neuromaps.parcellate
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.parcellate

.. autosummary::
   :template: class.rst
   :toctree: generated/

   neuromaps.parcellate.Parcellater

.. _ref_plotting:

:mod:`neuromaps.plotting` - Plotting functions
----------------------------------------------
.. automodule:: neuromaps.plotting
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.plotting

.. autosummary::
   :template: function.rst
   :toctree: generated/

   neuromaps.plotting.plot_surf_template

.. _ref_points:

:mod:`neuromaps.points` - Triangle mesh utilites
------------------------------------------------
.. automodule:: neuromaps.points
    :no-members:
    :no-inherited-members:

.. currentmodule:: neuromaps.points

.. autosummary::
    :template: function.rst
    :toctree: generated/

    neuromaps.points.make_surf_graph
    neuromaps.points.get_surface_distance

.. _ref_resampling:

:mod:`neuromaps.resampling` - Resampling workflows
--------------------------------------------------
.. automodule:: neuromaps.resampling
    :no-members:
    :no-inherited-members:

.. currentmodule:: neuromaps.resampling

.. autosummary::
    :template: function.rst
    :toctree: generated/

    neuromaps.resampling.resample_images

.. _ref_stats:

:mod:`neuromaps.stats` - Statistical functions
----------------------------------------------
.. automodule:: neuromaps.stats
    :no-members:
    :no-inherited-members:

.. currentmodule:: neuromaps.stats

.. autosummary::
    :template: function.rst
    :toctree: generated/

    neuromaps.stats.compare_images
    neuromaps.stats.permtest_metric

.. _ref_transforms:

:mod:`neuromaps.transforms` - Transformations between spaces
------------------------------------------------------------
.. automodule:: neuromaps.transforms
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.transforms

.. autosummary::
   :template: function.rst
   :toctree: generated/

   neuromaps.transforms.mni152_to_civet
   neuromaps.transforms.mni152_to_fsaverage
   neuromaps.transforms.mni152_to_fslr
   neuromaps.transforms.mni152_to_mni152

   neuromaps.transforms.civet_to_fslr
   neuromaps.transforms.fslr_to_civet
   neuromaps.transforms.civet_to_fsaverage
   neuromaps.transforms.fsaverage_to_civet
   neuromaps.transforms.civet_to_civet
   neuromaps.transforms.fslr_to_fsaverage
   neuromaps.transforms.fsaverage_to_fslr
   neuromaps.transforms.fslr_to_fslr
   neuromaps.transforms.fsaverage_to_fsaverage
