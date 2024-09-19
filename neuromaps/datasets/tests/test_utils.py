# -*- coding: utf-8 -*-
"""For testing neuromaps.datasets.utils functionality."""

import os
import pytest
import importlib.resources
from neuromaps.datasets import utils


def test_dataset_json():
    """Test loading dataset JSON."""
    from neuromaps.datasets.utils import \
        NEUROMAPS_DATASETS, NEUROMAPS_DATASETS_PUBLIC
    assert "spreng" not in [
        _["source"] for _ in NEUROMAPS_DATASETS_PUBLIC["annotations"]]
    assert "spreng" in [
        _["source"] for _ in NEUROMAPS_DATASETS["annotations"]]


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
    # handling pkg_resources.resource_filename deprecation
    if getattr(importlib.resources, 'files', None) is not None:
        osf = importlib.resources.files("neuromaps") / 'datasets/data/osf.json'
    else:
        from pkg_resources import resource_filename
        osf = resource_filename('neuromaps', 'datasets/data/osf.json')

    out = utils.parse_json(osf)
    assert isinstance(out, list) and all(isinstance(i, dict) for i in out)
