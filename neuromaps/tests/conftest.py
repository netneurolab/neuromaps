# -*- coding: utf-8 -*-
"""
Fixtures for all abagen tests
"""

import shutil

import pytest


def pytest_runtest_setup(item):
    markers = set(mark.name for mark in item.iter_markers())
    if 'workbench' in markers and shutil.which('wb_command') is None:
        pytest.skip('Cannot run without Connectome Workbench')


@pytest.fixture(scope='session')
def surfparc():
    from nilearn.datasets import fetch_atlas_surf_destrieux
    from neuromaps.images import construct_shape_gii, relabel_gifti

    destrieux = fetch_atlas_surf_destrieux()
    labels = [label.decode() for label in destrieux['labels']]
    parc_left = construct_shape_gii(destrieux['map_left'], labels=labels,
                                    intent='NIFTI_INTENT_LABEL')
    parc_right = construct_shape_gii(destrieux['map_right'], labels=labels,
                                     intent='NIFTI_INTENT_LABEL')
    parcellation = relabel_gifti((parc_left, parc_right),
                                 background=['Medial_wall'])

    return parcellation


@pytest.fixture(scope='session')
def volparc():
    from nilearn.datasets import fetch_atlas_schaefer_2018
    from neuromaps.images import load_nifti

    schaefer = fetch_atlas_schaefer_2018(n_rois=100, resolution_mm=2)

    return load_nifti(schaefer['maps'])
