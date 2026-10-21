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

Functions to show all available annotations

.. autosummary::
   :template: function.rst
   :toctree: generated/

   available_annotations
   available_tags

Functions to fetch and describe the annotations

.. autosummary::
   :template: function.rst
   :toctree: generated/

   fetch_annotation
   describe_annotations

Functions to fetch the atlases

.. autosummary::
   :template: function.rst
   :toctree: generated/

   fetch_atlas
   fetch_civet
   fetch_fsaverage
   fetch_fslr
   fetch_mni152
   fetch_regfusion
   fetch_all_atlases
   get_atlas_dir

.. _ref_images:

:mod:`neuromaps.images` - Image and surface handling
----------------------------------------------------
.. automodule:: neuromaps.images
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.images

Functions to load the images and surfaces

.. autosummary::
   :template: function.rst
   :toctree: generated/

   load_gifti
   load_nifti

Functions to convert surfaces to GIFTI format

.. autosummary::
   :template: function.rst
   :toctree: generated/

   relabel_gifti
   annot_to_gifti
   dlabel_to_gifti
   obj_to_gifti
   fssurf_to_gifti
   fsmorph_to_gifti

Functions to work with surfaces

.. autosummary::
   :template: function.rst
   :toctree: generated/

   average_surfaces
   interp_surface
   vertex_areas

.. _ref_nulls:

:mod:`neuromaps.nulls` - Null models
------------------------------------
.. automodule:: neuromaps.nulls
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.nulls

Spatial permutation null models (for surface images only)

.. autosummary::
   :template: function.rst
   :toctree: generated/

   alexander_bloch
   vazquez_rodriguez
   vasa
   hungarian
   baum
   cornblath

Parametric spatial null models (for volumetric and surface images)

.. autosummary::
   :template: function.rst
   :toctree: generated/

   burt2018
   burt2020
   moran

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

   Parcellater

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

   plot_surf_template

.. _ref_points:

:mod:`neuromaps.points` - Triangle mesh utilities
-------------------------------------------------
.. automodule:: neuromaps.points
    :no-members:
    :no-inherited-members:

.. currentmodule:: neuromaps.points

.. autosummary::
    :template: function.rst
    :toctree: generated/

    make_surf_graph
    get_surface_distance

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

    resample_images

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

    compare_images
    permtest_metric

.. _ref_transforms:

:mod:`neuromaps.transforms` - Transformations between spaces
------------------------------------------------------------
.. automodule:: neuromaps.transforms
   :no-members:
   :no-inherited-members:

.. currentmodule:: neuromaps.transforms

Volume-to-surface transformations

.. autosummary::
   :template: function.rst
   :toctree: generated/

   mni152_to_civet
   mni152_to_fsaverage
   mni152_to_fslr

Volume-to-volume transformations

.. autosummary::
   :template: function.rst
   :toctree: generated/

   mni152_to_mni152

Surface-to-surface transformations

.. autosummary::
   :template: function.rst
   :toctree: generated/

   civet_to_fslr
   fslr_to_civet
   civet_to_fsaverage
   fsaverage_to_civet
   civet_to_civet
   fslr_to_fsaverage
   fsaverage_to_fslr
   fslr_to_fslr
   fsaverage_to_fsaverage
