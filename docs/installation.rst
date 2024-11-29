.. _installation_setup:

----------------------
Installation and setup
----------------------

.. _installation_requirements:

Requirements
============

In order to effectively use ``neuromaps`` you must have the `Connectome
Workbench <https://www.humanconnectome.org/software/connectome-workbench>`_
installed and accessible on your computer. Large portions of the functionality
of the ``neuromaps`` toolbox rely on a few of the functions from the
Connectome Workbench. You can follow `instructions here
<https://www.humanconnectome.org/software/get-connectome-workbench>`_ for
installing it. Once you have installed it open your terminal and type

.. code-block:: bash

    wb_command -version

to make sure it is properly installed.

.. _basic_installation:

Basic installation
==================

Currently, ``neuromaps`` works with Python 3.8+.
You can install stable versions of ``neuromaps`` from PyPI with ``pip install neuromaps``.
However, we recommend installing from the source repository to get the latest features and bug fixes.

You can install ``neuromaps`` from the source repository with ``pip install git+https://github.com/netneurolab/neuromaps.git``
or by cloning the repository and installing from the local directory:

.. code-block:: bash

    git clone https://github.com/netneurolab/neuromaps
    cd neuromaps
    pip install .
