brainnotation
=============

The ``brainnotation`` toolbox is designed to help researchers make easy,
statistically-rigorous comparisons between brain maps (or brain annotations).

Installation requirements
-------------------------

Currently, ``brainnotation`` works with Python 3.7+ and requires a few
dependencies:

- matplotlib
- nibabel (>=3.0)
- nilearn (>=0.7)
- numpy (>=1.14)
- scikit-learn (>=0.17)
- scipy

You can get started by installing ``brainnotation`` from the source repository
with:

.. code-block:: bash

    git clone https://github.com/rmarkello/brainnotation
    cd brainnotation
    pip install brainnotation

You will also need to have `Connectome Workbench <https://www.humanconnectome.
org/software/connectome-workbench>`_ installed and available on your path in
order to use most of the transformation / resampling functionality of
``brainnotation``.

.. _installation:

License information
-------------------

This codebase is licensed under the `3-clause BSD license <https://opensource.
org/licenses/BSD-3-Clause>`_. The full license can be found in the
`LICENSE <https://github.com/netneurolab/brainnotation/blob/main/brainnotation
/LICENSE>`_ file in the ``brainnotation`` distribution.
