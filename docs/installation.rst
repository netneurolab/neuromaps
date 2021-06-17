.. _installation_setup:

----------------------
Installation and setup
----------------------

.. _installation_requirements:

Requirements
============

In order to effectively use `brainnotation` you must have the `Connectome
Workbench <https://www.humanconnectome.org/software/connectome-workbench>`_
installed and accesible on your computer. Large portions of the functionality
of the `brainnotation` toolbox rely on a few of the functions from the
Connectome Workbench. You can follow `instructions here
<https://www.humanconnectome.org/software/get-connectome-workbench>`_ for
installing it. Once you have installed it open your terminal and type

.. code-block:: bash

    wb_command -version

to make sure it is properly installed.

.. _basic_installation:

Basic installation
==================

This package requires Python 3.7+. Assuming you have the correct version of
Python installed, you can install ``brainnotation`` by opening a terminal and
running the following:

.. code-block:: bash

    pip install brainnotation

Alternatively, you can install the most up-to-date version of from GitHub:

.. code-block:: bash

   git clone https://github.com/netneurolab/brainnotation.git
   cd brainnotation
   pip install .
