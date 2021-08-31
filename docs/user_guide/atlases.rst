.. _usage_atlases:

Coordinate systems
==================

.. _usage_atlases_supported:

Supported coordinate systems
----------------------------

The ``neuromaps`` toolbox supports data in four standard coordinate systems:

  1. MNI152 (volumetric) space,
  2. fsLR (surface) space,
  3. fsaverage (surface) space, and
  4. CIVET (surface) space

`MNI152` space is an relatively arbitrary designation. Here, when we refer to
the MNI152 coordinate system we are referencing the variation of the MNI ICBM
152 non-linear 6th generation symmetric template provided with FSL and used
throughout the Minn/Wash-U Human Connectome Project processing pipelines. On
the other hand, `fsLR` space refers to the surface-based coordinate system
originally developed by the Minn/Wash-U Human Connectome Project; `fsaverage`
refers to the surface-based coordinate system used throughout FreeSurfer; and
`CIVET` refers to the surface-based coordinate system derived from the MNI152
volumetric template and is used in the CIVET processing software.

All of these coordinate systems have multiple resolutions (or densities), and
the ``neuromaps`` distributions supports data in the following representations:

  1. MNI152: 1mm, 2mm, 3mm (isotropic voxel sizes)
  2. fsLR: 4k, 8k, 32k, 164k (number of vertices per hemisphere)
  3. fsaverage: 1k, 3k, 10k, 41k, 164k (number of vertices per hemisphere)
  4. CIVET: 41k (number of vertices per hemisphere)

.. _usage_atlases_access:

Accessing coordinate systems
----------------------------

In order to access the templates for the coordinate systems provided with
``neuromaps`` you can use the :func:`neuromaps.datasets.fetch_atlas` function.
This function accepts two positional arguments: (1) the name of the standard
coordinate system you want, and (2) a density (for surface-based systems) or
resolution (for volumetric systems). The returned object will be a dictionary
whose keys will depend on the specified system.

For volumetric systems (i.e., the MNI152 system), the object will have the
following keys:

.. code-block::

    >>> from neuromaps.datasets import fetch_atlas
    >>> mni152 = fetch_atlas('MNI152', '1mm')
    >>> print(sorted(mni152))
    ['CSF', 'GM', 'PD', 'T1w', 'T2w', 'WM', 'brainmask']

The corresponding values in the ``mni151`` dictionary all point to gzipped
NIFTI files that contain data relevant to the specified key (i.e., probability
maps for 'CSF', 'GM', and 'WM', whole-brain images for 'T1w' [T1-weighted],
'T2w' [T2-weighted], and 'PD' [proton density'], and a brain mask for
'brainmask'). These files can all be loaded with ``nibabel``:

.. code-block::
x
    >>> import nibabel as nib
    >>> brainmask = nib.load(mni152['brainmask'])
    >>> print(brainmask.shape)
    (193, 229, 193)

For surface-based systems (i.e., the fsLR, fsaverage, and CIVET systems), the
keys in the returned object will vary slightly; however, all of these atlases
will have the following keys: 'inflated', 'sphere', 'medial', 'sulc', and
'vaavg'. Here, 'inflated' and 'sphere' refer to two different representations
of the surface mesh, 'medial' is a mask where vertices of the surface along the
medial wall have values of 1, 'sulc' provides sulcal depth information
calculated from the relevant surface, and 'vaavg' is the average vertex area
for each vertex of the surface mesh (derived from a group of participants from
the Human Connectome Project).

.. code-block::

    >>> fslr = fetch_atlas('fsLR', '32k')
    >>> print(sorted(fslr))
    ['inflated', 'medial', 'midthickness', 'sphere', 'sulc', 'vaavg', 'veryinflated']

The corresponding values of these keys are all named tuples of GIFTI files
(with fields 'L' and 'R' for the left and right hemisphere files). These files
can be loaded using ``nibabel``:

.. code-block::

    >>> fslr_left_infl = nib.load(fslr['inflated'].L)
    >>> vertices = fslr_left_infl.agg_data('NIFTI_INTENT_POINTSET')
    >>> print(vertices.shape[0])
    32492

