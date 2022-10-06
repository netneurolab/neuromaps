.. image:: neuromaps_logo.png

The ``neuromaps`` toolbox is designed to help researchers make easy,
statistically-rigorous comparisons between brain maps (or brain annotations).

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
If you use data included in the ``neuromaps`` repository, be sure to cite the original paper that published this data.
A table with references for each brain map can be found in the Wiki.

License information
-------------------

This work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ``cc-by-nc-sa``.
The full license can be found in the
`LICENSE <https://github.com/netneurolab/neuromaps/blob/main/neuromaps
/LICENSE>`_ file in the ``neuromaps`` distribution.
