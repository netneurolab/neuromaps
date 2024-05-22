# -*- coding: utf-8 -*-
"""For testing neuromaps.datasets.utils functionality."""

import os
import pytest
from pkg_resources import resource_filename
from neuromaps.datasets import utils


@pytest.mark.xfail
def test__osfify_urls():
    """Test osfifying urls."""
    assert False


@pytest.mark.xfail
def test_get_dataset_info():
    """Test getting dataset info."""
    assert False


@pytest.mark.xfail
def test_get_data_dir():
    """Test getting the data directory."""
    assert False


def test__get_token():
    """Test getting the OSF token."""
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
    """Test getting the OSF session."""
    assert False


@pytest.mark.xfail
def test_parse_filename():
    """Test parsing filenames."""
    assert False


@pytest.mark.xfail
def test_parse_fname_list():
    """Test parsing filename lists."""
    assert False


def test_parse_json():
    """Test parsing JSON files."""
    osf = resource_filename('neuromaps', 'datasets/data/osf.json')
    out = utils.parse_json(osf)
    assert isinstance(out, list) and all(isinstance(i, dict) for i in out)
