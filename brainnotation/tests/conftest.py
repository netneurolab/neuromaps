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
