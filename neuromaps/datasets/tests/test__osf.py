# -*- coding: utf-8 -*-
"""
For testing neuromaps.datasets._osf functionality
"""

from pkg_resources import resource_filename

import pytest

from neuromaps.datasets import _osf


@pytest.mark.xfail
def test_parse_filename():
    assert False


@pytest.mark.xfail
def test_parse_fname_list():
    assert False


def test_parse_json():
    osf = resource_filename('neuromaps', 'datasets/data/osf.json')
    out = _osf.parse_json(osf)
    assert isinstance(out, list) and all(isinstance(i, dict) for i in out)


@pytest.mark.xfail
def test_write_json():
    assert False


@pytest.mark.xfail
def test_complete_json():
    assert False


@pytest.mark.xfail
def test_check_missing_keys():
    assert False


@pytest.mark.xfail
def test_generate_auto_keys():
    assert False


@pytest.mark.xfail
def test_clean_minimal_keys():
    assert False


@pytest.mark.xfail
def test_get_url():
    assert False


@pytest.mark.xfail
def test_generate_release_json():
    assert False
