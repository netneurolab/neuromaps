.. _usage_annotations:

Brain maps and annotations
==========================

Beyond standard atlases, the ``neuromaps`` toolbox offers access to a
repository of brain maps (which we frequently refer to as brain annotations).
These annotations are spatial maps representing some feature of interest and
are available in at least one of the four standard coordinate systems.

We have curated a set of brain annotations that we make available through a
standard interface.
More details about each annotation can be found in our `Wiki 
<https://github.com/netneurolab/neuromaps/wiki/Annotation-information>`_.

.. important::

    ``neuromaps`` curates data that was acquired by other groups.
    If you fetch data from ``neuromaps``, please cite the accompanying
    papers listed for each annotation in the `Wiki
    <https://github.com/netneurolab/neuromaps/wiki/Annotation-information>`_.
    
You can search for available annotations using the
:func:`neuromaps.datasets.available_annotations` function:

.. code-block::

    >>> from neuromaps.datasets import available_annotations
    >>> for annotation in available_annotations():
    ...     print(annotation)
    ('abagen', 'genepc1', 'fsaverage', '10k')
    ('margulies2016', 'fcgradient01', 'fsLR', '32k')
    ('margulies2016', 'fcgradient02', 'fsLR', '32k')
    ('margulies2016', 'fcgradient03', 'fsLR', '32k')
    ('margulies2016', 'fcgradient04', 'fsLR', '32k')
    ('margulies2016', 'fcgradient05', 'fsLR', '32k')
    ('margulies2016', 'fcgradient06', 'fsLR', '32k')
    ('margulies2016', 'fcgradient07', 'fsLR', '32k')
    ('margulies2016', 'fcgradient08', 'fsLR', '32k')
    ('margulies2016', 'fcgradient09', 'fsLR', '32k')
    ('margulies2016', 'fcgradient10', 'fsLR', '32k')
    ('neurosynth', 'cogpc1', 'MNI152', '2mm')

Annotations are identified by a len-4 tuple of values. The first entry in the
tuple corresponds to the "source" of the annotation. This is typically a
shorthand reference to a published journal article (e.g., ``'margulies2016'``
refers to the article Margulies et al., 2016, *PNAS*); however, it can also
refer to e.g., a software toolbox (i.e., ``abagen`` and ``neurosynth``). The
second entry in the tuple provides a brief description of what the map
represents. (Because these descriptors are encoded directly in the filenames of
the relevant maps we are somewhat limited in terms of space.) The last two
entries in the tuple correspond to the coordinate system and density/resolution
in which the annotations are provided.

This function also accepts keyword arguments in case we want to narrow down the
list of returned annotations:

.. code-block::

    >>> for annotation in available_annotations(source='abagen'):
    ...     print(annotation)
    ('abagen', 'genepc1', 'fsaverage', '10k')

Moreover, most annotations have "tags" that help to describe the data they
represent. You can see what tags are available using the
:func:`neuromaps.datasets.available_tags` function, and then search for
annotations using your desired tag(s):

.. code-block::

    >>> from neuromaps.datasets import available_tags
    >>> print(available_tags())
    >>> for annotation in available_annotations(tags=['genetics']):
    ...     print(annotation)
    ('abagen', 'genepc1', 'fsaverage', '10k')

Refer to the API of :func:`neuromaps.datasets.available_annotations` for all
possible keywords that can be used when searching for available annotations.

To actually fetch one of these annotations we can use the
:func:`neuromaps.datasets.fetch_annotation` function, which accepts the same
keyword arguments:

.. code-block::

    >>> from neuromaps.datasets import fetch_annotation
    >>> annotation = fetch_annotation(source='neurosynth')
    >>> print(annotation)
    /.../neuromaps-data/annotations/neurosynth/cogpc1/MNI152/source-neurosynth_desc-cogpc1_space-MNI152_res-2mm_feature.nii.gz

Brain annotations are, by default, downloaded to a sub-directory of
``$HOME/neuromaps-data``; however, you can specify the ``data_dir`` keyword or
set an environmental variable (``$NEUROMAPS_DATA``) to control where the
annotations are downloaded.

You can fetch multiple annotations at once by passing lists to any of the
relevant keyword arguments. However, note that you will get back a dictionary
where the keys are the len-4 tuples discussed above and the values are the
corresponding filepaths to the brain annotations:

.. code-block::

    >>> annotations = fetch_annotation(source=['abagen', 'neurosynth'])
    >>> print(sorted(annotations))
    [('abagen', 'genepc1', 'fsaverage', '10k'), ('neurosynth', 'cogpc1', 'MNI152', '2mm')]
    >>> print(annotations[('abagen', 'genepc1', 'fsaverage', '10k')])
    ['/.../neuromaps-data/annotations/abagen/genepc1/fsaverage/source-abagen_desc-genepc1_space-fsaverage_den-10k_hemi-L_feature.func.gii', '/.../neuromaps-data/annotations/abagen/genepc1/fsaverage/source-abagen_desc-genepc1_space-fsaverage_den-10k_hemi-R_feature.func.gii']
    >>> print(annotations[('neurosynth', 'cogpc1', 'MNI152', '2mm')])
    /.../neuromaps-data/annotations/neurosynth/cogpc1/MNI152/source-neurosynth_desc-cogpc1_space-MNI152_res-2mm_feature.nii.gz

If you would prefer for :func:`~.datasets.fetch_annotation` to always return a
dictionary you can pass the ``return_single=False`` keyword argument. Refer to
the API for more information on other parameters.
