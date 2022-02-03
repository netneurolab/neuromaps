# -*- coding: utf-8 -*-
"""
For testing neuromaps.workflows functionality
"""

import numpy as np
import pytest

from neuromaps import datasets, workflows


@pytest.mark.workbench
@pytest.mark.parametrize('annot, space, parcellation', [
    (datasets.fetch_annotation(source='abagen'), 'fsaverage', None),
    (np.random.rand(148), 'fsaverage', 'surfparc'),
    (np.random.rand(100), 'MNI152', 'volparc')
])
def test_basic_Analyis(volparc, surfparc, annot, space, parcellation):
    targets = datasets.available_annotations(source='raichle',
                                             desc=['cbf', 'cbv'])

    kwargs = {}
    if parcellation is not None:
        parcs = {'surfparc': surfparc, 'volparc': volparc}
        kwargs = dict(parcellation=parcs.get(parcellation))

    # check that outputs are generated
    wf = workflows.Analysis(annot, space, targets, n_perm=0, **kwargs)
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

    # now try with nulls (if not volumetric)
    if space == 'MNI152':
        return

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
