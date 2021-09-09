# -*- coding: utf-8 -*-
"""
For testing neuromaps.parcellate functionality
"""

import pytest


@pytest.mark.xfail
def test__gifti_to_array():
    assert False


@pytest.mark.xfail
def test__array_to_gifti():
    assert False


@pytest.mark.xfail
@pytest.mark.workbench
def test_surfparc_Parcellater(surfparc):
    assert False


@pytest.mark.xfail
def test_volparc_Parcellater(volparc):
    assert False
