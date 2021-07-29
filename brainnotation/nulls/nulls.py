# -*- coding: utf-8 -*-
"""
Contains functionality for running spatial null models
"""

import numpy as np

try:
    from brainsmash.mapgen import Base, Sampled
    _brainsmash_avail = True
except ImportError:
    _brainsmash_avail = False
try:
    from brainspace.null_models.moran import MoranRandomization
    _brainspace_avail = True
except ImportError:
    _brainspace_avail = False
from sklearn.utils.validation import check_random_state

from brainnotation.datasets import fetch_atlas
from brainnotation.images import load_gifti, PARCIGNORE
from brainnotation.points import get_surface_distance
from brainnotation.nulls.burt import batch_surrogates
from brainnotation.nulls.spins import (gen_spinsamples, get_parcel_centroids,
                                       load_spins, spin_data, spin_parcels)
HEMI = dict(left='L', lh='L', right='R', rh='R')


_nulls_input_docs = dict(
    data_or_none="""\
data : (N,) array_like
    Input data from which to generate null maps. If None is provided then the
    resampling array will be returned instead.\
""",
    data="""\
data : (N,) array_like
    Input data from which to generate null maps\
""",
    atlas_density="""\
atlas : {'fsLR', 'fsaverage', 'civet'}, optional
    Name of surface atlas on which `data` are defined. Default: 'fsaverage'
density : str, optional
    Density of surface mesh on which `data` are defined. Must be
    compatible with specified `atlas`. Default: '10k'\
""",
    parcellation="""\
parcellation : tuple-of-str or os.PathLike, optional
    Filepaths to parcellation images ([left, right] hemisphere) mapping `data`
    to surface mesh specified by `atlas` and `density`. Should only be supplied
    if `data` represents a parcellated null map. Default: None\
""",
    n_perm="""\
n_perm : int, optional
    Number of null maps or permutations to generate. Default: 1000\
""",
    seed="""\
seed : {int, np.random.RandomState instance, None}, optional
    Seed for random number generation. Default: None\
""",
    spins="""\
spins : array_like or str or os.PathLike
    Filepath to or pre-loaded resampling array. If not specified spins are
    generated. Default: None\
""",
    surfaces="""\
surfaces : tuple-of-str or os.PathLike, optional
    Instead of specifying `atlas` and `density` this specifies the surface
    files on which `data` are defined. Providing this will override arguments
    supplied to `atlas` and `density`. Default: None
""",
    n_proc="""\
n_proc : int, optional
    Number of processors to use for parallelizing computations. If negative
    will use max available processors plus 1 minus the specified number.
    Default: 1 (no parallelization)\
""",
    distmat="""\
distmat : tuple-of-str or os.PathLike, optional
    Filepaths to pre-computed (left, right) surface distance matrices.
    Providing this will cause `atlas`, `density`, and `parcellation` to be
    ignored. Default: None\
""",
    kwargs="""\
kwargs : key-value pairs
    Other keyword arguments passed directly to the underlying null method
    generator\
""",
    nulls="""\
nulls : np.ndarray
    Generated null distribution, where each column represents a unique null
    map\
"""
)


def naive_nonparametric(data, atlas='fsaverage', density='10k',
                        parcellation=None, n_perm=1000, seed=None, spins=None,
                        surfaces=None):
    rs = check_random_state(seed)
    if spins is None:
        if data is None:
            if surfaces is None:
                surfaces = fetch_atlas(atlas, density)['sphere']
            coords, _ = get_parcel_centroids(surfaces,
                                             parcellation=parcellation,
                                             method='surface')
        else:
            coords = np.asarray(data)
        spins = np.column_stack([
            rs.permutation(len(coords)) for _ in range(n_perm)
        ])
    spins = load_spins(spins)
    if data is None:
        data = np.arange(len(spins))
    return np.asarray(data)[spins]


naive_nonparametric.__doc__ = """\
Generates null maps from `data` using naive non-parametric method

Method uses random permutations of `data` with no consideration for spatial
topology to generate null distribution

Parameters
----------
{data_or_none}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{spins}
{surfaces}

Returns
-------
{nulls}
""".format(**_nulls_input_docs)


def alexander_bloch(data, atlas='fsaverage', density='10k', parcellation=None,
                    n_perm=1000, seed=None, spins=None, surfaces=None):
    if spins is None:
        if surfaces is None:
            surfaces = fetch_atlas(atlas, density)['sphere']
        coords, hemi = get_parcel_centroids(surfaces,
                                            parcellation=parcellation,
                                            method='surface')
        spins = gen_spinsamples(coords, hemi, n_rotate=n_perm, seed=seed)
    spins = load_spins(spins)
    if data is None:
        data = np.arange(len(spins))
    return np.asarray(data)[spins]


alexander_bloch.__doc__ = """\
Generates null maps from `data` using method from [SN1]_

Method projects data to a spherical surface and uses arbitrary rotations to
generate null distribution. If `data` are parcellated then parcel centroids
are projected to surface and parcels are reassigned based on minimum distances.

Parameters
----------
{data_or_none}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{spins}
{surfaces}

Returns
-------
{nulls}

References
----------
.. [SN1] Alexander-Bloch, A., Shou, H., Liu, S., Satterthwaite, T. D.,
   Glahn, D. C., Shinohara, R. T., Vandekar, S. N., & Raznahan, A. (2018).
   On testing for spatial correspondence between maps of human brain
   structure and function. NeuroImage, 178, 540-51.
""".format(**_nulls_input_docs)


vazquez_rodriguez = alexander_bloch


def vasa(data, atlas='fsaverage', density='10k', parcellation=None,
         n_perm=1000, seed=None, spins=None, surfaces=None):
    if parcellation is None:
        raise ValueError('Cannot use `vasa()` null method without specifying '
                         'a parcellation. Use `alexander_bloch() instead if '
                         'working with unparcellated data.')
    if spins is None:
        if surfaces is None:
            surfaces = fetch_atlas(atlas, density)['sphere']
        coords, hemi = get_parcel_centroids(surfaces,
                                            parcellation=parcellation,
                                            method='surface')
        spins = gen_spinsamples(coords, hemi, method='vasa', n_rotate=n_perm,
                                seed=seed)
    spins = load_spins(spins)
    if data is None:
        data = np.arange(len(spins))
    return np.asarray(data)[spins]


vasa.__doc__ = """\
Generates null maps for parcellated `data` using method from [SN2]_

Method projects parcels to a spherical surface and uses arbitrary rotations
with iterative reassignments to generate null distribution. All nulls are
"perfect" permutations of the input data (at the slight expense of spatial
topology)

Parameters
----------
{data_or_none}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{spins}
{surfaces}

Returns
-------
{nulls}

References
----------
.. [SN2] Váša, F., Seidlitz, J., Romero-Garcia, R., Whitaker, K. J.,
   Rosenthal, G., Vértes, P. E., ... & Jones, P. B. (2018). Adolescent
   tuning of association cortex in human structural brain networks.
   Cerebral Cortex, 28(1), 281-294.
""".format(**_nulls_input_docs)


def hungarian(data, atlas='fsaverage', density='10k', parcellation=None,
              n_perm=1000, seed=None, spins=None, surfaces=None):
    if parcellation is None:
        raise ValueError('Cannot use `hungarian()` null method without '
                         'specifying a parcellation. Use `alexander_bloch() '
                         'instead if working with unparcellated data.')
    if spins is None:
        if surfaces is None:
            surfaces = fetch_atlas(atlas, density)['sphere']
        coords, hemi = get_parcel_centroids(surfaces,
                                            parcellation=parcellation,
                                            method='surface')
        spins = gen_spinsamples(coords, hemi, method='hungarian',
                                n_rotate=n_perm, seed=seed)
    spins = load_spins(spins)
    if data is None:
        data = np.arange(len(spins))
    return np.asarray(data)[spins]


hungarian.__doc__ = """\
Generates null maps for parcellated `data` using the Hungarian method ([SN3]_)

Method projects parcels to a spherical surface and uses arbitrary rotations
with reassignments based on optimization via the Hungarian method to generate
null distribution. All nulls are "perfect" permutations of the input data (at
the slight expense of spatial topology)

Parameters
----------
{data_or_none}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{spins}
{surfaces}

Returns
-------
{nulls}

References
----------
.. [SN3] Kuhn, H. W. (1955). The Hungarian method for the assignment problem.
   Naval Research Logistics Quarterly, 2(1‐2), 83-97.
""".format(**_nulls_input_docs)


def baum(data, atlas='fsaverage', density='10k', parcellation=None,
         n_perm=1000, seed=None, spins=None, surfaces=None):
    if parcellation is None:
        raise ValueError('Cannot use `baum()` null method without specifying '
                         'a parcellation. Use `alexander_bloch() instead if '
                         'working with unparcellated data.')
    y = np.asarray(data)
    if surfaces is None:
        surfaces = fetch_atlas(atlas, density)['sphere']
    spins = spin_parcels(surfaces, parcellation,
                         n_rotate=n_perm, spins=spins, seed=seed)
    if data is None:
        data = np.arange(len(spins))
    y = np.asarray(data)
    nulls = y[spins]
    nulls[spins == -1] = np.nan
    return nulls


baum.__doc__ = """\
Generates null maps for parcellated `data` using method from [SN4]_

Method projects `data` to spherical surface and uses arbitrary rotations to
generate null distributions. Reassigned parcels are based on the most common
(i.e., modal) value of the vertices in each parcel within the the rotated data

Parameters
----------
{data_or_none}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{spins}
{surfaces}

Returns
-------
{nulls}

References
----------
.. [SN4] Baum, G. L., Cui, Z., Roalf, D. R., Ciric, R., Betzel, R. F., Larsen,
   B., ... & Satterthwaite, T. D. (2020). Development of structure–function
   coupling in human brain networks during youth. Proceedings of the National
   Academy of Sciences, 117(1), 771-778.
""".format(**_nulls_input_docs)


def cornblath(data, atlas='fsaverage', density='10k', parcellation=None,
              n_perm=1000, seed=None, spins=None, surfaces=None):
    if parcellation is None:
        raise ValueError('Cannot use `cornblath()` null method without '
                         'specifying a parcellation. Use `alexander_bloch() '
                         'instead if working with unparcellated data.')
    y = np.asarray(data)
    if surfaces is None:
        surfaces = fetch_atlas(atlas, density)['sphere']
    nulls = spin_data(y, surfaces, parcellation,
                      n_rotate=n_perm, spins=spins, seed=seed)
    return nulls


cornblath.__doc__ = """\
Generates null maps for parcellated `data` using method from [SN5]_

Method projects `data` to spherical surface and uses arbitrary rotations to
generate null distributions. Reassigned parcels are based on the average value
of the vertices in each parcel within the rotated data

Parameters
----------
{data}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{spins}
{surfaces}

Returns
-------
{nulls}

References
----------
.. [SN5] Cornblath, E. J., Ashourvan, A., Kim, J. Z., Betzel, R. F., Ciric, R.,
   Adebimpe, A., ... & Bassett, D. S. (2020). Temporal sequences of brain
   activity at rest are constrained by white matter structure and modulated by
   cognitive demands. Communications biology, 3(1), 1-12.
""".format(**_nulls_input_docs)


def _get_distmat(hemisphere, atlas='fsaverage', density='10k',
                 parcellation=None, drop=None, n_proc=1):
    hemi = HEMI.get(hemisphere, hemisphere)
    if hemi not in ('L', 'R'):
        raise ValueError(f'Invalid hemishere designation {hemisphere}')

    if drop is None:
        drop = PARCIGNORE

    atlas = fetch_atlas(atlas, density)
    surf, medial = getattr(atlas['pial'], hemi), getattr(atlas['medial'], hemi)
    if parcellation is None:
        dist = get_surface_distance(surf, medial=medial, n_proc=n_proc)
    else:
        dist = get_surface_distance(surf, parcellation=parcellation,
                                    medial_labels=drop, drop=drop,
                                    n_proc=n_proc)
    return dist


_get_distmat.__doc__ = """\
Generates surface distance matrix for specified `hemisphere`

If `parcellation` is provided then the returned distance matrix will be a
parcel-parcel matrix.

Parameters
----------
hemisphere : {{'L', 'R'}}
    Hemisphere of surface from which to generate distance matrix
{atlas_density}
{parcellation}
drop : list-of-str, optional
    If `parcellation` is not None, which parcels should be ignored / dropped
    from the generate distance matrix. If not specified will ignore parcels
    generally indicative of the medial wall. Default: None
{n_proc}

Returns
-------
dist : (N, N) np.ndarray
    Surface distance matrix between vertices. If a `parcellation` is specified
    then this will be the parcel-parcel distance matrix, where the distance
    between parcels is the average distance between all constituent vertices
""".format(**_nulls_input_docs)


def _make_surrogates(data, method, atlas='fsaverage', density='10k',
                     parcellation=None, n_perm=1000, seed=None, distmat=None,
                     n_proc=1, **kwargs):
    if method not in ('burt2018', 'burt2020', 'moran'):
        raise ValueError(f'Invalid null method: {method}')

    darr = np.asarray(data)
    dmin = darr[np.logical_not(np.isnan(darr))].min()
    if parcellation is None:
        parcellation = (None, None)

    surrogates = np.zeros((len(data), n_perm))
    for n, (hemi, parc) in enumerate(zip(('L', 'R'), parcellation)):
        if distmat is None:
            dist = _get_distmat(hemi, atlas=atlas, density=density,
                                parcellation=parc, n_proc=n_proc)
        else:
            dist = distmat[n]

        if parc is None:
            idx = np.arange(n * (len(data) // 2), (n + 1) * (len(data) // 2))
        else:
            idx = np.unique(load_gifti(parc).agg_data())[1:]

        hdata = np.squeeze(data[idx])
        mask = np.logical_not(np.isnan(hdata))
        surrogates[idx[np.logical_not(mask)]] = np.nan
        hdata, dist, idx = hdata[mask], dist[np.ix_(mask, mask)], idx[mask]

        if method == 'burt2018':
            hdata += np.abs(dmin) + 0.1
            surrogates[idx] = batch_surrogates(dist, hdata, n_surr=n_perm,
                                               seed=seed)
        elif method == 'burt2020':
            if parc is None:
                index = np.argsort(dist, axis=-1)
                dist = np.sort(dist, axis=-1)
                surrogates[idx] = \
                    Sampled(hdata, dist, index, n_jobs=n_proc,
                            seed=seed, **kwargs)(n_perm).T
            else:
                surrogates[idx] = \
                    Base(hdata, dist, seed=seed, **kwargs)(n_perm, 50).T
        elif method == 'moran':
            dist = dist.astype('float64')
            np.fill_diagonal(dist, 1)
            dist **= -1
            opts = dict(joint=True, tol=1e-6, n_rep=n_perm, random_state=seed)
            opts.update(**kwargs)
            mrs = MoranRandomization(**kwargs)
            surrogates[idx] = mrs.fit(dist).randomize(hdata).T

    return surrogates


_make_surrogates.__doc__ = """\
Generates null surrogates for specified `data` using `method`

Parameters
----------
{data}
method : {{'burt2018', 'burt2020', 'moran'}}
    Method by which to generate null surrogates
{atlas_density}
{parcellation}
{n_perm}
{seed}
{distmat}
{n_proc}
{kwargs}

Returns
-------
{nulls}
""".format(**_nulls_input_docs)


def burt2018(data, atlas='fsaverage', density='10k', parcellation=None,
             n_perm=1000, seed=None, distmat=None, n_proc=1, **kwargs):
    if not _brainsmash_avail:
        raise ImportError('Cannot run burt2018 null model when `brainsmash` '
                          'is not installed. Please `pip install brainsmash` '
                          'and try again.')
    return _make_surrogates(data, 'burt2018', atlas=atlas, density=density,
                            parcellation=parcellation, n_perm=n_perm,
                            seed=seed, n_proc=n_proc, distmat=distmat,
                            **kwargs)


burt2018.__doc__ = """\
Generates null maps for `data` using method from [SN6]_

Method uses a spatial auto-regressive model to estimate distance-dependent
relationship of `data` and generates surrogate maps with similar properties

Parameters
----------
{data}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{distmat}
{kwargs}

Returns
-------
{nulls}

References
----------
.. [SN6] Burt, J. B., Demirtaş, M., Eckner, W. J., Navejar, N. M., Ji, J. L.,
   Martin, W. J., ... & Murray, J. D. (2018). Hierarchy of transcriptomic
   specialization across human cortex captured by structural neuroimaging
   topography. Nature Neuroscience, 21(9), 1251-1259.
""".format(**_nulls_input_docs)


def burt2020(data, atlas='fsaverage', density='10k', parcellation=None,
             n_perm=1000, seed=None, distmat=None, n_proc=1, **kwargs):
    if not _brainsmash_avail:
        raise ImportError('Cannot run burt2020 null model when `brainsmash` '
                          'is not installed. Please `pip install brainsmash` '
                          'and try again.')
    return _make_surrogates(data, 'burt2020', atlas=atlas, density=density,
                            parcellation=parcellation, n_perm=n_perm,
                            seed=seed, n_proc=n_proc, distmat=distmat,
                            **kwargs)


burt2020.__doc__ = """\
Generates null maps for `data` using method from [SN7]_ and [SN8]_

Method uses variograms to estimate spatial autocorrelation of `data` and
generates surrogate maps with similar variogram properties

Parameters
----------
{data}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{n_proc}
{distmat}
{kwargs}

Returns
-------
{nulls}

References
----------
.. [SN7] Burt, J. B., Helmer, M., Shinn, M., Anticevic, A., & Murray, J. D.
   (2020). Generative modeling of brain maps with spatial autocorrelation.
   NeuroImage, 220, 117038.
.. [SN8] https://github.com/murraylab/brainsmash
""".format(**_nulls_input_docs)


def moran(data, atlas='fsaverage', density='10k', parcellation=None,
          n_perm=1000, seed=None, distmat=None, n_proc=1, **kwargs):
    if not _brainspace_avail:
        raise ImportError('Cannot run moran null model when `brainspace` is '
                          'not installed. Please `pip install brainspace` and '
                          'try again.')
    return _make_surrogates(data, 'moran', atlas=atlas, density=density,
                            parcellation=parcellation, n_perm=n_perm,
                            seed=seed, n_proc=n_proc, distmat=distmat,
                            **kwargs)


moran.__doc__ = """\
Generates null maps for `data` using method from [SN9]_

Method uses a spatial decomposition of a distance-based weight matrix to
estimate eigenvectors that are used to generate surrogate maps by imposing a
similar spatial structure on randomized data. For a MATLAB implementation
refer to [SN10]_ and [SN11]_

Parameters
----------
{data}
{atlas_density}
{parcellation}
{n_perm}
{seed}
{n_proc}
{distmat}
{kwargs}

Returns
-------
{nulls}

References
----------
.. [SN9] Wagner, H. H., & Dray, S. (2015). Generating spatially constrained
   null models for irregularly spaced data using M oran spectral randomization
   methods. Methods in Ecology and Evolution, 6(10), 1169-1178.
.. [SN10] de Wael, R. V., Benkarim, O., Paquola, C., Lariviere, S., Royer, J.,
   Tavakol, S., ... & Bernhardt, B. C. (2020). BrainSpace: a toolbox for the
   analysis of macroscale gradients in neuroimaging and connectomics datasets.
   Communications Biology, 3(1), 1-10.
.. [SN11] https://github.com/MICA-MNI/BrainSpace/
""".format(**_nulls_input_docs)
