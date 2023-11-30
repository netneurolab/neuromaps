# -*- coding: utf-8 -*-
"""For testing neuromaps.datasets.annotations functionality."""

import pytest

from neuromaps.datasets import annotations


@pytest.mark.xfail
def test__groupby_match():
    """Test grouping by matching values."""
    assert False


@pytest.mark.xfail
def test__match_annot():
    """Test matching annotations."""
    assert False


@pytest.mark.xfail
def test_available_annotations():
    """Test available annotations."""
    assert False


def test_available_tags():
    """Test available tags."""
    unrestricted = annotations.available_tags()
    restricted = annotations.available_tags(return_restricted=True)
    assert isinstance(unrestricted, list) and isinstance(restricted, list)
    assert all(f in restricted for f in unrestricted)


@pytest.mark.xfail
def test_fetch_annotation():
    """Test fetching an annotation."""
    assert False
