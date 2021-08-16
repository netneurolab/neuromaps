# -*- coding: utf-8 -*-
"""
For testing neuromaps.datasets.annotations functionality
"""

import pytest

from neuromaps.datasets import annotations


@pytest.mark.xfail
def test__groupby_match():
    assert False


@pytest.mark.xfail
def test__match_annot():
    assert False


@pytest.mark.xfail
def test_available_annotations():
    assert False


def test_available_tags():
    unrestricted = annotations.available_tags()
    restricted = annotations.available_tags(return_restricted=True)
    assert isinstance(unrestricted, list) and isinstance(restricted, list)
    assert all(f in restricted for f in unrestricted)


@pytest.mark.xfail
def test_fetch_annotation():
    assert False
