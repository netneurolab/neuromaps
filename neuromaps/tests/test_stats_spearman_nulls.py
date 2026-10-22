"""Regression tests for rank-consistent observed and supplied-null statistics."""
import numpy as np
import pytest
from numpy.testing import assert_allclose, assert_array_equal
from scipy.stats import spearmanr, rankdata, pearsonr
from neuromaps import stats


def reference(a, b, nulls, nan_policy='propagate'):
    r = spearmanr(a, b, nan_policy=nan_policy)[0]
    d = np.array([spearmanr(c, b, nan_policy=nan_policy)[0]
                  for c in nulls.T])
    if not np.isfinite(r) or not np.all(np.isfinite(d)):
        p = np.nan
    else:
        threshold = abs(r) - 100 * np.finfo(float).eps * abs(r)
        p = (1 + np.count_nonzero(abs(d) >= threshold)) / (len(d) + 1)
    return r, p, d


def ring_fixture():
    n = 100
    theta = 2 * np.pi * np.arange(n) / n
    base = 2 + np.sin(theta + .123) + .17 * np.sin(3 * theta + .257)
    a = rankdata(base)
    a[a == n] = 1e8  # Strictly increasing rescaling of distinct source ranks.
    b = 2 + np.sin(theta + 1.111) + .13 * np.cos(2 * theta + .421)
    nulls = np.column_stack([np.roll(a, k) for k in range(1, n)])
    return a, b, nulls


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
@pytest.mark.parametrize('seed', range(10))
def test_external_nulls_match_independent_spearman(entry, seed):
    rng = np.random.default_rng(seed)
    a = rng.lognormal(0, 2, 31)
    b = rng.normal(size=31)
    nulls = np.column_stack([rng.permutation(a) for _ in range(29)])
    actual = getattr(stats, entry)(a, b, metric='spearmanr', nulls=nulls,
                                   return_nulls=True)
    expected = reference(a, b, nulls)
    for x, y in zip(actual, expected):
        assert_allclose(x, y, rtol=1e-12, atol=1e-14)


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
def test_circular_shift_significance_and_monotonic_invariance(entry):
    a, b, nulls = ring_fixture()
    f = getattr(stats, entry)
    raw = f(a, b, metric='spearmanr', nulls=nulls, return_nulls=True)
    ranked = f(rankdata(a), b, metric='spearmanr',
               nulls=rankdata(nulls, axis=0), return_nulls=True)
    expected = reference(a, b, nulls)
    assert_allclose(raw[0], .5778217821782178, atol=1e-14)
    assert_allclose(raw[1], .60, atol=1e-14)
    for x, y, z in zip(raw, ranked, expected):
        assert_allclose(x, y, atol=1e-14)
        assert_allclose(x, z, atol=1e-14)


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
def test_ties_and_identity_draw(entry):
    a = np.array([1., 1., 2., 4., 4., 4., 8., 9.])
    b = np.array([1., 3., 3., 6., 6., 9., 7., 9.])
    nulls = np.column_stack([a, a[::-1], np.roll(a, 2), np.roll(a, 3)])
    result = getattr(stats, entry)(a, b, metric='spearmanr', nulls=nulls,
                                   return_nulls=True)
    for x, y in zip(result, reference(a, b, nulls)):
        assert_allclose(x, y, atol=1e-14)


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
def test_null_specific_nan_omission_ranks_on_pairwise_support(entry):
    a = np.array([1., 3., 2., 7., 4., 9., 8., 10.])
    b = np.array([5., 1., 6., 2., 8., 4., 9., 10.])
    nulls = np.column_stack([np.roll(a, k) for k in (1, 2, 3)])
    nulls[[1, 3, 6], [0, 1, 2]] = np.nan
    result = getattr(stats, entry)(a, b, metric='spearmanr', nulls=nulls,
                                   nan_policy='omit', return_nulls=True)
    for x, y in zip(result, reference(a, b, nulls, 'omit')):
        assert_allclose(x, y, atol=1e-14)


def test_observed_nan_omission_direct():
    a = np.array([1., np.nan, 3., 8., 4., 9., 7.])
    b = np.array([2., 5., 4., 3., np.nan, 9., 8.])
    nulls = np.column_stack([np.roll(a, k) for k in (1, 2, 3)])
    actual = stats.permtest_metric(a, b, metric='spearmanr', nulls=nulls,
                                   nan_policy='omit', return_nulls=True)
    for x, y in zip(actual, reference(a, b, nulls, 'omit')):
        assert_allclose(x, y, atol=1e-14)


def test_compare_mask_applied_before_ranking_nulls():
    a = np.array([0., 1., 3., 2., 7., 4., 9., 8., np.nan])
    b = np.array([9., 5., 1., 6., 2., 8., 4., 9., 10.])
    nulls = np.column_stack([np.roll(np.nan_to_num(a, nan=10.), k)
                            for k in (1, 2, 3)])
    mask = ~np.isclose(a, 0) & ~np.isnan(a)
    actual = stats.compare_images(a, b, metric='spearmanr', nulls=nulls,
                                   return_nulls=True)
    for x, y in zip(actual, reference(a[mask], b[mask], nulls[mask])):
        assert_allclose(x, y, atol=1e-14)


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
def test_nan_raise_accepts_finite_inputs_and_rejects_nan(entry):
    a, b, nulls = ring_fixture()
    f = getattr(stats, entry)
    result = f(a, b, metric='spearmanr', nulls=nulls, nan_policy='raise')
    assert_allclose(result[1], .60)
    nulls[0, 0] = np.nan
    with pytest.raises(ValueError, match='nan'):
        f(a, b, metric='spearmanr', nulls=nulls, nan_policy='raise')


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
@pytest.mark.parametrize('where', ['observed', 'null'])
def test_undefined_statistic_does_not_produce_significant_p(entry, where):
    a, b, nulls = ring_fixture()
    if where == 'observed':
        b[:] = 1.0
    else:
        nulls[:, 0] = 1.0
    result = getattr(stats, entry)(a, b, metric='spearmanr', nulls=nulls)
    assert np.isnan(result[1])


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
def test_nan_propagate_does_not_produce_significant_p(entry):
    a, b, nulls = ring_fixture()
    nulls[0, 0] = np.nan
    result = getattr(stats, entry)(a, b, metric='spearmanr', nulls=nulls,
                                   nan_policy='propagate')
    assert np.isnan(result[1])


def test_internal_and_equivalent_external_permutations_match():
    a, b, _ = ring_fixture()
    rng = np.random.RandomState(42)
    nulls = np.column_stack([a[rng.permutation(len(a))] for _ in range(31)])
    internal = stats.permtest_metric(a, b, metric='spearmanr', n_perm=31,
                                    seed=42, return_nulls=True)
    external = stats.permtest_metric(a, b, metric='spearmanr', nulls=nulls,
                                    return_nulls=True)
    for x, y in zip(internal, external):
        assert_allclose(x, y, atol=1e-14)


def test_spearman_matching_columns_and_broadcasting():
    rng = np.random.default_rng(43)
    a = rng.lognormal(size=(15, 2))
    b = rng.normal(size=(15, 1))
    actual = stats.permtest_metric(a, b, metric='spearmanr', n_perm=17,
                                   return_nulls=True)
    expected = [stats.permtest_metric(a[:, j], b[:, 0], metric='spearmanr',
                                     n_perm=17, return_nulls=True)
                for j in range(2)]
    assert_allclose(actual[0], [x[0] for x in expected])
    assert_allclose(actual[1], [x[1] for x in expected])
    assert_allclose(actual[2], np.column_stack([x[2] for x in expected]))


@pytest.mark.parametrize('policy', ['omit', 'propagate', 'raise'])
def test_compare_without_nulls(policy):
    a, b, _ = ring_fixture()
    actual = stats.compare_images(a, b, metric='spearmanr', nan_policy=policy)
    assert_allclose(actual, spearmanr(a, b)[0], atol=1e-14)


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
def test_inputs_not_mutated(entry):
    a, b, nulls = ring_fixture()
    before = [x.copy() for x in (a, b, nulls)]
    for x in (a, b, nulls):
        x.flags.writeable = False
    getattr(stats, entry)(a, b, metric='spearmanr', nulls=nulls)
    for x, y in zip((a, b, nulls), before):
        assert_array_equal(x, y)


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
def test_invalid_nan_policy(entry):
    a, b, nulls = ring_fixture()
    with pytest.raises(ValueError, match='nan_policy'):
        getattr(stats, entry)(a, b, metric='spearmanr', nulls=nulls,
                              nan_policy='invalid')


def test_pearson_external_nulls_unchanged():
    rng = np.random.default_rng(4321)
    a, b = rng.normal(size=(2, 25))
    nulls = rng.normal(size=(25, 19))
    r, p, d = stats.permtest_metric(a, b, metric='pearsonr', nulls=nulls,
                                   return_nulls=True)
    ref_r = pearsonr(a, b)[0]
    ref_d = np.array([pearsonr(v, b)[0] for v in nulls.T])
    ref_p = (1 + sum(abs(ref_d) >= abs(ref_r))) / 20
    assert_allclose(r, ref_r)
    assert_allclose(d, ref_d)
    assert_allclose(p, ref_p)


def test_custom_callable_not_rank_transformed():
    a = np.arange(1., 10.) ** 2
    b = np.arange(2., 11.)
    nulls = np.column_stack([a[::-1], np.roll(a, 3)])
    metric = lambda x, y: np.mean(x * y)
    actual = stats.permtest_metric(a, b, metric=metric, nulls=nulls,
                                   return_nulls=True)
    assert_allclose(actual[0], metric(a, b))
    assert_allclose(actual[2], [metric(v, b) for v in nulls.T])


def test_callable_workaround_avoids_affected_string_dispatch():
    a, b, nulls = ring_fixture()
    metric = lambda x, y: spearmanr(x, y)[0]
    actual = stats.compare_images(a, b, metric=metric, nulls=nulls,
                                   return_nulls=True)
    for x, y in zip(actual, reference(a, b, nulls)):
        assert_allclose(x, y, atol=1e-14)


@pytest.mark.parametrize('entry', ['permtest_metric', 'compare_images'])
def test_scalar_inputs_return_scalar_statistics(entry):
    a, b, nulls = ring_fixture()
    r, p = getattr(stats, entry)(a, b, metric='spearmanr', nulls=nulls)
    assert np.isscalar(r)
    assert np.isscalar(p)
