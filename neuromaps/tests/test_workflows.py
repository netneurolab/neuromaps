# -*- coding: utf-8 -*-
"""
For testing neuromaps.workflows functionality
"""

import numpy as np
import pytest

from neuromaps import datasets, workflows


@pytest.mark.workbench
def test_basic_Analyis():
    space = 'fsaverage'
    annot = datasets.fetch_annotation(source='abagen', space=space)
    targets = datasets.available_annotations(source='raichle',
                                             desc=['cbf', 'cbv'])

    # check that outputs are generated
    wf = workflows.Analysis(annot, space, targets, n_perm=0)
    out = wf.run()
    assert isinstance(out, list) and len(out) == len(targets)

    # check that outputs have expected format
    for n, (target, stats) in enumerate(out):
        assert targets[n] == target
        assert isinstance(stats, float)

    # check that outputs are cached
    hsh1 = wf._gen_hash()
    assert hsh1 in wf._stats
    assert list(wf._stats[hsh1].items()) == out

    # now try with nulls
    wf.n_perm = 10
    out = wf.run()

    # check that outputs have expected format
    for n, (target, stats) in enumerate(out):
        assert targets[n] == target
        assert isinstance(stats, tuple)
        assert len(stats) == 2
        assert all(isinstance(stat, float) for stat in stats)

    # check that outputs are cached
    hsh2 = wf._gen_hash()
    assert hsh1 != hsh2
    assert all(hsh in wf._stats for hsh in (hsh1, hsh2))
    assert list(wf._stats[hsh2].items()) == out


@pytest.mark.workbench
def test_surfparc_Analysis(surfparc):
    space = 'fsaverage'
    data = np.random.rand(148)
    targets = datasets.available_annotations(source='raichle',
                                             desc=['cbf', 'cbv'])

    # check that outputs are generated
    wf = workflows.Analysis(data, space, targets, parcellation=surfparc,
                            n_perm=0)
    out = wf.run()
    assert isinstance(out, list) and len(out) == len(targets)

    # check that outputs have expected format
    for n, (target, stats) in enumerate(out):
        assert targets[n] == target
        assert isinstance(stats, float)

    # check that outputs are cached
    hsh1 = wf._gen_hash()
    assert hsh1 in wf._stats
    assert list(wf._stats[hsh1].items()) == out

    # now try with nulls
    wf.n_perm = 10
    out = wf.run()

    # check that outputs have expected format
    for n, (target, stats) in enumerate(out):
        assert targets[n] == target
        assert isinstance(stats, tuple)
        assert len(stats) == 2
        assert all(isinstance(stat, float) for stat in stats)

    # check that outputs are cached
    hsh2 = wf._gen_hash()
    assert hsh1 != hsh2
    assert all(hsh in wf._stats for hsh in (hsh1, hsh2))
    assert list(wf._stats[hsh2].items()) == out


def test_volparc_Analysis(volparc):
    space = 'MNI152'
    data = np.random.rand(100)
    targets = datasets.available_annotations(source='raichle',
                                             desc=['cbf', 'cbv'])

    # check that outputs are generated
    wf = workflows.Analysis(data, space, targets, parcellation=volparc,
                            n_perm=0)
    out = wf.run()
    assert isinstance(out, list) and len(out) == len(targets)

    # check that outputs have expected format
    for n, (target, stats) in enumerate(out):
        assert targets[n] == target
        assert isinstance(stats, float)

    # check that outputs are cached
    hsh1 = wf._gen_hash()
    assert hsh1 in wf._stats
    assert list(wf._stats[hsh1].items()) == out

    # # now try with nulls
    # wf.n_perm = 10
    # out = wf.run()

    # # check that outputs have expected format
    # for n, (target, stats) in enumerate(out):
    #     assert targets[n] == target
    #     assert isinstance(stats, tuple)
    #     assert len(stats) == 2
    #     assert all(isinstance(stat, float) for stat in stats)

    # # check that outputs are cached
    # hsh2 = wf._gen_hash()
    # assert hsh1 != hsh2
    # assert all(hsh in wf._stats for hsh in (hsh1, hsh2))
    # assert list(wf._stats[hsh2].items()) == out
