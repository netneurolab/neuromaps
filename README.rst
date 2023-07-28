.. image:: neuromaps_logo.png

The ``neuromaps`` toolbox is designed to help researchers make easy,
statistically-rigorous comparisons between brain maps (or brain annotations).
Documentation can be found `here <https://netneurolab.github.io/neuromaps/>`_.

The accompanying paper is published in `Nature Methods <https://www.nature.com/articles/s41592-022-01625-w>`_.

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5842499.svg
   :target: https://doi.org/10.5281/zenodo.5842499

Installation requirements
-------------------------

Currently, ``neuromaps`` works with Python 3.7+ and requires a few
dependencies:

- matplotlib
- nibabel (>=3.0)
- nilearn (>=0.7)
- numpy (>=1.14)
- scikit-learn (>=0.17)
- scipy

You can get started by installing ``neuromaps`` from the source repository
with:

.. code-block:: bash

    git clone https://github.com/netneurolab/neuromaps
    cd neuromaps
    pip install .

You will also need to have `Connectome Workbench <https://www.humanconnectome.
org/software/connectome-workbench>`_ installed and available on your path in
order to use most of the transformation / resampling functionality of
``neuromaps``.

.. _installation:

Citation
--------

If you use the ``neuromaps`` toolbox, please cite our `paper <https://www.nature.com/articles/s41592-022-01625-w>`_.
**Importantly**, ``neuromaps`` implements and builds on tools that have been previously developed, and we redistribute data that was acquired elsewhere.
Please be sure to cite the appropriate literature when using ``neuromaps``, which we detail below.

- If you use volume-to-surface transformations (registration fusion), please cite `Buckner et al 2011 <https://journals.physiology.org/doi/full/10.1152/jn.00339.2011>`_ (original proposition) and `Wu et al 2018 <https://onlinelibrary.wiley.com/doi/10.1002/hbm.24213>`_ (first implementation of MNI152 to fsaverage transformation).
- If you use surface-to-surface transformations (multimodal surface matching), please cite `Robinson et al 2014 <https://www.sciencedirect.com/science/article/pii/S1053811914004546?via%3Dihub>`_ and `Robinson et al 2018 <https://www.sciencedirect.com/science/article/pii/S1053811917308649?via%3Dihub>`_.
- If you use data included in ``neuromaps``, please cite the the original papers that publish the data. A table with references for each brain annotation can be found in our `wiki <https://github.com/netneurolab/neuromaps/wiki>`_, or more specifically, at `this <https://docs.google.com/spreadsheets/d/1oZecOsvtQEh5pQkIf8cB6CyhPKVrQuko/edit?rtpof=true&sd=true#gid=1162991686>`_ link.
- If you use the spatial null models, there is an associated citation with each type of null model. They can be found in the docstring of the function, and also `here <https://netneurolab.github.io/neuromaps/api.html#module-neuromaps.nulls>`_. 

License information
-------------------

This work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ``cc-by-nc-sa``.
The full license can be found in the
`LICENSE <https://github.com/netneurolab/neuromaps/blob/main/neuromaps
/LICENSE>`_ file in the ``neuromaps`` distribution.
