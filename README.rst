.. image:: https://github.com/netneurolab/neuromaps/raw/main/docs/_static/neuromaps_logo.png

|

.. image:: https://zenodo.org/badge/375755159.svg
   :target: https://zenodo.org/badge/latestdoi/375755159
   :alt: Zenodo record

.. image:: https://img.shields.io/pypi/v/neuromaps
   :target: https://pypi.python.org/pypi/neuromaps/
   :alt: Latest PyPI version

.. image:: https://img.shields.io/badge/docker-netneurolab/neuromaps-brightgreen.svg?logo=docker&style=flat
  :target: https://hub.docker.com/r/netneurolab/neuromaps/tags/
  :alt: Latest Docker image

.. image:: https://github.com/netneurolab/neuromaps/actions/workflows/tests.yml/badge.svg
  :target: https://github.com/netneurolab/neuromaps/actions/workflows/tests.yml
  :alt: run-tests status

.. image:: https://github.com/netneurolab/neuromaps/actions/workflows/docs.yml/badge.svg
  :target: https://netneurolab.github.io/neuromaps/
  :alt: deploy-docs status

|

The ``neuromaps`` toolbox is designed to help researchers make easy,
statistically-rigorous comparisons between brain maps (or brain annotations).
Documentation can be found `here <https://netneurolab.github.io/neuromaps/>`_.

The accompanying paper is published in `Nature Methods <https://www.nature.com/articles/s41592-022-01625-w>`_ (`postprint <https://github.com/netneurolab/neuromaps/blob/main/markello2022natmethods.pdf>`_).

Check all the brain maps we have `here <https://netneurolab.github.io/neuromaps/listofmaps.html>`_!

Features
--------

- A growing library of brain maps ("annotations") in their original coordinate space, including microstructure, function, electrophysiology, receptors, and more
- Robust transforms between MNI-152, fsaverage, fsLR, and CIVET spaces
- Integrated spatial null models for statistically assessing correspondences between brain maps

.. image:: https://github.com/netneurolab/neuromaps/raw/main/docs/_static/neuromaps_features.png


Installation requirements
-------------------------

Currently, ``neuromaps`` works with Python 3.8+.
You can install stable versions of ``neuromaps`` from PyPI with ``pip install neuromaps``.
However, we recommend installing from the source repository to get the latest features and bug fixes.

You can install ``neuromaps`` from the source repository with ``pip install git+https://github.com/netneurolab/neuromaps.git``
or by cloning the repository and installing from the local directory:

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

**Importantly**, ``neuromaps`` implements and builds on tools that have been previously developed, and we redistribute data that was acquired elsewhere.
If you use the ``neuromaps`` toolbox, please ensure proper attribution of the original data sources. Here's a quick checklist:

- Cite the ``neuromaps`` `paper <https://www.nature.com/articles/s41592-022-01625-w>`_.
- Cite the original papers that publish the data you are using. A complete list with references for each brain annotation can be found `in the documentation <https://netneurolab.github.io/neuromaps/listofmaps.html>`_, or `in this Google Sheet <https://docs.google.com/spreadsheets/d/1oZecOsvtQEh5pQkIf8cB6CyhPKVrQuko/edit?rtpof=true&sd=true#gid=1162991686>`_. We also provide a standalone bibliography file and a helper function to generate the citations.
- Cite the transformations used

  - Volume-to-surface transformations (registration fusion): `Buckner et al 2011 <https://journals.physiology.org/doi/full/10.1152/jn.00339.2011>`_ (original proposition) and `Wu et al 2018 <https://onlinelibrary.wiley.com/doi/10.1002/hbm.24213>`_ (first implementation of MNI152 to fsaverage transformation).
  - Surface-to-surface transformations (multimodal surface matching): `Robinson et al 2014 <https://www.sciencedirect.com/science/article/pii/S1053811914004546>`_ and `Robinson et al 2018 <https://www.sciencedirect.com/science/article/pii/S1053811917308649>`_.

- Cite the spatial null models used (see API documentation)

License information
-------------------

This work is licensed under a
Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License ``cc-by-nc-sa``.
The full license can be found in the
`LICENSE <https://github.com/netneurolab/neuromaps/blob/main/neuromaps
/LICENSE>`_ file in the ``neuromaps`` distribution.
