.. _contributing:

----------------------------
Contributing a new brain map
----------------------------

We are always looking to expand the ``neuromaps`` toolbox with more data!
This data should be shared in the original format that it was gathered, 
at the surface (fsaverage, fsLR, or CIVET) or volumetric (MNI-152) format.
In the case of surface data, hemispheres should be in separate files.

Surface files should be named according to this format: 
``source-[source]_desc-[description]_space-[space]_den-[density]_hemi-[hemisphere]_feature.func.gii``.

Volumetric files should be named according to this format: 
``source-[source]_desc-[description]_space-MNI152_res-[resolution]_feature.nii.gz``.

The source of the data is typically the last name of the first author 
on the paper that first presents the data, followed by the year of the 
paper's publication. Alternatively, it could be the name of the toolbox 
that generated the data. Here are four examples:

``source-reardon2018_desc-scalingpnc_space-civet_den-41k_hemi-L_feature.func.gii``

``source-abagen_desc-genepc1_space-fsaverage_den-10k_hemi-R_feature.func.gii``

``source-satterthwaite2014_desc-meancbf_space-MNI152_res-1mm_feature.nii.gz``

``source-sydnor2021_desc-SAaxis_space-fsLR_den-32k_hemi-L_feature.func.gii``

Note that the surface based maps would be accompanied with a second file 
with the other hemisphere.

New brain maps can be contributed to ``neuromaps`` using the 
:func:`neuromaps.datasets.contributions.upload_annotation` function.

.. code-block::

    >>> from neuromaps.datasets.contributions import upload_annotation
    >>> files = ["path/to/files"]  # tuple of all the files you want to upload
    >>> upload_annotation(files, "your.email@institution.com")

If this returns a response object of ``200``, it worked!
Note that your data will not be integrated with neuromaps until the maintainers 
have approved of the data.
