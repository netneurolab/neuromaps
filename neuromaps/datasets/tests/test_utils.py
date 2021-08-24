# -*- coding: utf-8 -*-
"""
For testing neuromaps.datasets.utils functionality
"""

import os
import pytest

from neuromaps.datasets import utils


@pytest.mark.xfail
def test__osfify_urls():
    assert False


@pytest.mark.xfail
def test_get_dataset_info():
    assert False


@pytest.mark.xfail
def test_get_data_dir():
    assert False


def test__get_token():
    orig = os.environ.pop('NEUROMAPS_OSF_TOKEN', None)
    assert utils._get_token(None) is None
    assert utils._get_token('test') == 'test'
    os.environ['NEUROMAPS_OSF_TOKEN'] = 'test_env'
    assert utils._get_token(None) == 'test_env'
    assert utils._get_token('test') == 'test'
    if orig is not None:  # reset env variable
        os.environ['NEUROMAPS_OSF_TOKEN'] = orig


@pytest.mark.xfail
def test__get_session():
    assert False
