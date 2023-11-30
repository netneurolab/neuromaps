# -*- coding: utf-8 -*-
"""For testing neuromaps.datasets._osf functionality."""

from pkg_resources import resource_filename

import pytest

from neuromaps.datasets import _osf


@pytest.mark.xfail
def test_parse_filename():
    """Test parsing a filename."""
    assert False


@pytest.mark.xfail
def test_parse_fname_list():
    """Test parsing a list of filenames."""
    assert False


def test_parse_json():
    """Test parsing a JSON file."""
    osf = resource_filename('neuromaps', 'datasets/data/osf.json')
    out = _osf.parse_json(osf)
    assert isinstance(out, list) and all(isinstance(i, dict) for i in out)


@pytest.mark.xfail
def test_write_json():
    """Test writing a JSON file."""
    assert False


@pytest.mark.xfail
def test_complete_json():
    """Test completing a JSON file."""
    assert False


@pytest.mark.xfail
def test_check_missing_keys():
    """Test checking for missing keys."""
    assert False


@pytest.mark.xfail
def test_generate_auto_keys():
    """Test generating automatic keys."""
    assert False


@pytest.mark.xfail
def test_clean_minimal_keys():
    """Test cleaning minimal keys."""
    assert False


@pytest.mark.xfail
def test_get_url():
    """Test getting a URL."""
    assert False


@pytest.mark.xfail
def test_generate_release_json():
    """Test generating a release JSON file."""
    assert False
