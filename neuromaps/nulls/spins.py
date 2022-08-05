# -*- coding: utf-8 -*-
"""
Contains helper code for running spatial nulls models
"""

from pathlib import Path
import warnings

import numpy as np
from scipy import optimize, spatial
try:  # scipy >= 1.8.0
    from scipy.ndimage._measurements import _stats, labeled_comprehension
except ImportError:  # scipy < 1.8.0
    from scipy.ndimage.measurements import _stats, labeled_comprehension
from sklearn.utils.validation import check_random_state

from neuromaps.images import load_gifti, PARCIGNORE
from neuromaps.points import _geodesic_parcel_centroid


def load_spins(fn, n_perm=None):
    """
    Loads spins from `fn`

    Parameters
    ----------
    fn : os.PathLike
        Filepath to file containing spins to load
    n_perm : int, optional
        Number of spins to retain (i.e., subset data)

    Returns
    -------
    spins : (N, P) array_like
        Loaded spins
    """

    try:
        npy = Path(fn).with_suffix('.npy')
        if npy.exists():
            spins = np.load(npy, allow_pickle=False, mmap_mode='c')
        else:
            spins = np.loadtxt(fn, delimiter=',', dtype='int32')
    except TypeError:
        spins = np.asarray(fn, dtype='int32')

    if n_perm is not None:
        spins = spins[..., :n_perm]

    return spins


def get_parcel_centroids(surfaces, parcellation=None, method='surface',
                         drop=None):
    """
    Returns vertex coordinates corresponding to parcel centroids

    If `parcellation` is not specified then returned `centroids` are vertex
    coordinates of `surfaces`

    Parameters
    ----------
    surfaces : (2,) list-of-str
        Surfaces on which to compute parcel centroids; generally spherical
        surfaces are recommended. Surfaces should be (left, right) hemisphere.
        If no parcellations are provided then returned `centroids` represent
        all vertices in `surfaces`
    parcellation : (2,) list-of-str, optional
        Path to GIFTI label files containing labels of parcels on the
        (left, right) hemisphere. If not specified then vertex coordinates from
        `surfaces` are returned instead. Default: None
    method : {'average', 'surface', 'geodesic'}, optional
        Method for calculation of parcel centroid. See Notes for more
        information. Default: 'surface'
    drop : list, optional
        Specifies regions in `parcellation` for which the parcel centroid
        should not be calculated. If not specified, centroids for parcels
        defined in `PARCIGNORE` are not calculated. Default: None

    Returns
    -------
    centroids : (N, 3) numpy.ndarray
        Coordinates of parcel centroids. If `parcellation` is not specified
        these are simply the vertex coordinates
    hemiid : (N,) numpy.ndarray
        Array denoting hemisphere designation of coordinates in `centroids`,
        where `hemiid=0` denotes the left and `hemiid=1` the right hemisphere

    Notes
    -----
    The following methods can be used for finding parcel centroids:

    1. ``method='average'``

       Uses the arithmetic mean of the coordinates for the vertices in each
       parcel. Note that in this case the calculated centroids will not act
       actually fall on the surface of `surf`.

    2. ``method='surface'``

       Calculates the 'average' coordinates and then finds the closest vertex
       on `surf`, where closest is defined as the vertex with the minimum
       Euclidean distance.

    3. ``method='geodesic'``

       Uses the coordinates of the vertex with the minimum average geodesic
       distance to all other vertices in the parcel. Note that this is slightly
       more time-consuming than the other two methods, especially for
       high-resolution meshes.
    """

    methods = ['average', 'surface', 'geodesic']
    if method not in methods:
        raise ValueError('Provided method for centroid calculation {} is '
                         'invalid. Must be one of {}'.format(methods, methods))

    if drop is None:
        drop = PARCIGNORE
    if parcellation is None:
        parcellation = (None, None)

    centroids, hemiid = [], []
    for n, (parc, surf) in enumerate(zip(parcellation, surfaces)):
        vertices, faces = load_gifti(surf).agg_data()
        if parc is not None:
            labels = load_gifti(parc).agg_data()
            labeltable = parc.labeltable.get_labels_as_dict()

            for lab in np.unique(labels):
                if labeltable.get(lab) in drop:
                    continue

                mask = labels == lab
                if method in ('average', 'surface'):
                    roi = np.atleast_2d(vertices[mask].mean(axis=0))
                    if method == 'surface':  # find closest vertex on surf
                        idx = np.argmin(spatial.distance_matrix(vertices, roi),
                                        axis=0)[0]
                        roi = vertices[idx]
                elif method == 'geodesic':
                    inds, = np.where(mask)
                    roi = _geodesic_parcel_centroid(vertices, faces, inds)

                centroids.append(roi)
                hemiid.append(n)
        else:
            centroids.append(vertices)
            hemiid.extend([n] * len(vertices))

    return np.row_stack(centroids), np.asarray(hemiid)


def _gen_rotation(seed=None):
    """
    Generates random matrix for rotating spherical coordinates

    Parameters
    ----------
    seed : {int, np.random.RandomState instance, None}, optional
        Seed for random number generation

    Returns
    -------
    rotate_{l,r} : (3, 3) numpy.ndarray
        Rotations for left and right hemisphere coordinates, respectively
    """

    rs = check_random_state(seed)

    # for reflecting across Y-Z plane
    reflect = np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # generate rotation for left
    rotate_l, temp = np.linalg.qr(rs.normal(size=(3, 3)))
    rotate_l = rotate_l @ np.diag(np.sign(np.diag(temp)))
    if np.linalg.det(rotate_l) < 0:
        rotate_l[:, 0] = -rotate_l[:, 0]

    # reflect the left rotation across Y-Z plane
    rotate_r = reflect @ rotate_l @ reflect

    return rotate_l, rotate_r


def gen_spinsamples(coords, hemiid, n_rotate=1000, check_duplicates=True,
                    method='original', seed=None, verbose=False,
                    return_cost=False):
    """
    Returns a resampling array for `coords` obtained from rotations / spins

    Using the method initially proposed in [ST1]_ (and later modified + updated
    based on findings in [ST2]_ and [ST3]_), this function applies random
    rotations to the user-supplied `coords` in order to generate a resampling
    array that preserves its spatial embedding. Rotations are generated for one
    hemisphere and mirrored for the other (see `hemiid` for more information).

    Due to irregular sampling of `coords` and the randomness of the rotations
    it is possible that some "rotations" may resample with replacement (i.e.,
    will not be a true permutation). The likelihood of this can be reduced by
    either increasing the sampling density of `coords` or changing the
    ``method`` parameter (see Notes for more information on the latter).

    Parameters
    ----------
    coords : (N, 3) array_like
        X, Y, Z coordinates of `N` nodes/parcels/regions/vertices defined on a
        sphere
    hemiid : (N,) array_like
        Array denoting hemisphere designation of coordinates in `coords`, where
        values should be {0, 1} denoting the different hemispheres. Rotations
        are generated for one hemisphere and mirrored across the y-axis for the
        other hemisphere.
    n_rotate : int, optional
        Number of rotations to generate. Default: 1000
    check_duplicates : bool, optional
        Whether to check for and attempt to avoid duplicate resamplings. A
        warnings will be raised if duplicates cannot be avoided. Setting to
        True may increase the runtime of this function! Default: True
    method : {'original', 'vasa', 'hungarian'}, optional
        Method by which to match non- and rotated coordinates. Specifying
        'original' will use the method described in [ST1]_. Specfying 'vasa'
        will use the method described in [ST4]_. Specfying 'hungarian' will use
        the Hungarian algorithm to minimize the global cost of reassignment
        (will dramatically increase runtime). Default: 'original'
    seed : {int, np.random.RandomState instance, None}, optional
        Seed for random number generation. Default: None
    verbose : bool, optional
        Whether to print occasional status messages. Default: False
    return_cost : bool, optional
        Whether to return cost array (specified as Euclidean distance) for each
        coordinate for each rotation Default: True

    Returns
    -------
    spinsamples : (N, `n_rotate`) numpy.ndarray
        Resampling matrix to use in permuting data based on supplied `coords`.
    cost : (N, `n_rotate`,) numpy.ndarray
        Cost (specified as Euclidean distance) of re-assigning each coordinate
        for every rotation in `spinsamples`. Only provided if `return_cost` is
        True.

    Notes
    -----
    By default, this function uses the minimum Euclidean distance between the
    original coordinates and the new, rotated coordinates to generate a
    resampling array after each spin. Unfortunately, this can (with some
    frequency) lead to multiple coordinates being re-assigned the same value:

        >>> from neuromaps.nulls.spins import gen_spinsamples
        >>> coords = [[0, 0, 1], [1, 0, 0], [0, 0, 1], [1, 0, 0]]
        >>> hemi = [0, 0, 1, 1]
        >>> gen_spinsamples(coords, hemi, n_rotate=1, seed=1,
        ...                 check_duplicates=False)
        array([[0],
               [0],
               [2],
               [3]])

    While this is reasonable in most circumstances, if you feel incredibly
    strongly about having a perfect "permutation" (i.e., all indices appear
    once and exactly once in the resampling), you can set the ``method``
    parameter to either 'vasa' or 'hungarian':

        >>> gen_spinsamples(coords, hemi, n_rotate=1, seed=1,
        ...                 method='vasa', check_duplicates=False)
        array([[1],
               [0],
               [2],
               [3]])
        >>> gen_spinsamples(coords, hemi, n_rotate=1, seed=1,
        ...                 method='hungarian', check_duplicates=False)
        array([[0],
               [1],
               [2],
               [3]])

    Note that setting this parameter may increase the runtime of the function
    (especially for `method='hungarian'`). Refer to [ST1]_ for information on
    why the default suffices in most cases.

    For the original MATLAB implementation of this function refer to [ST5]_.

    References
    ----------
    .. [ST1] Alexander-Bloch, A., Shou, H., Liu, S., Satterthwaite, T. D.,
       Glahn, D. C., Shinohara, R. T., Vandekar, S. N., & Raznahan, A. (2018).
       On testing for spatial correspondence between maps of human brain
       structure and function. NeuroImage, 178, 540-51.

    .. [ST2] Blaser, R., & Fryzlewicz, P. (2016). Random Rotation Ensembles.
       Journal of Machine Learning Research, 17(4), 1–26.

    .. [ST3] Lefèvre, J., Pepe, A., Muscato, J., De Guio, F., Girard, N.,
       Auzias, G., & Germanaud, D. (2018). SPANOL (SPectral ANalysis of Lobes):
       A Spectral Clustering Framework for Individual and Group Parcellation of
       Cortical Surfaces in Lobes. Frontiers in Neuroscience, 12, 354.

    .. [ST4] Váša, F., Seidlitz, J., Romero-Garcia, R., Whitaker, K. J.,
       Rosenthal, G., Vértes, P. E., ... & Jones, P. B. (2018). Adolescent
       tuning of association cortex in human structural brain networks.
       Cerebral Cortex, 28(1), 281-294.

    .. [ST5] https://github.com/spin-test/spin-test
    """

    methods = ['original', 'vasa', 'hungarian']
    if method not in methods:
        raise ValueError('Provided method "{}" invalid. Must be one of {}.'
                         .format(method, methods))

    seed = check_random_state(seed)

    coords = np.asanyarray(coords)
    hemiid = np.squeeze(np.asanyarray(hemiid, dtype='int8'))

    # check supplied coordinate shape
    if coords.shape[-1] != 3 or coords.squeeze().ndim != 2:
        raise ValueError('Provided `coords` must be of shape (N, 3), not {}'
                         .format(coords.shape))

    # ensure hemisphere designation array is correct
    if hemiid.ndim != 1:
        raise ValueError('Provided `hemiid` array must be one-dimensional.')
    if len(coords) != len(hemiid):
        raise ValueError('Provided `coords` and `hemiid` must have the same '
                         'length. Provided lengths: coords = {}, hemiid = {}'
                         .format(len(coords), len(hemiid)))
    if np.max(hemiid) > 1 or np.min(hemiid) < 0:
        raise ValueError('Hemiid must have values in {0, 1} denoting left and '
                         'right hemisphere coordinates, respectively. '
                         + 'Provided array contains values: {}'
                         .format(np.unique(hemiid)))

    # empty array to store resampling indices
    spinsamples = np.zeros((len(coords), n_rotate), dtype=int)
    cost = np.zeros((len(coords), n_rotate))
    inds = np.arange(len(coords), dtype=int)

    # generate rotations and resampling array!
    msg, warned = '', False
    for n in range(n_rotate):
        count, duplicated = 0, True

        if verbose:
            msg = 'Generating spin {:>5} of {:>5}'.format(n, n_rotate)
            print(msg, end='\r', flush=True)

        while duplicated and count < 500:
            count, duplicated = count + 1, False
            resampled = np.zeros(len(coords), dtype='int32')

            # rotate each hemisphere separately
            for h, rot in enumerate(_gen_rotation(seed=seed)):
                hinds = (hemiid == h)
                coor = coords[hinds]
                if len(coor) == 0:
                    continue

                # if we need an "exact" mapping (i.e., each node needs to be
                # assigned EXACTLY once) then we have to calculate the full
                # distance matrix which is a nightmare with respect to memory
                # for anything that isn't parcellated data.
                # that is, don't do this with vertex coordinates!
                if method == 'vasa':
                    dist = spatial.distance_matrix(coor, coor @ rot)
                    # min of max a la Vasa et al., 2018
                    col = np.zeros(len(coor), dtype='int32')
                    for r in range(len(dist)):
                        # find parcel whose closest neighbor is farthest away
                        # overall; assign to that
                        row = dist.min(axis=1).argmax()
                        col[row] = dist[row].argmin()
                        cost[inds[hinds][row], n] = dist[row, col[row]]
                        # set to -inf and inf so they can't be assigned again
                        dist[row] = -np.inf
                        dist[:, col[row]] = np.inf
                # optimization of total cost using Hungarian algorithm. this
                # may result in certain parcels having higher cost than with
                # `method='vasa'` but should always result in the total cost
                # being lower #tradeoffs
                elif method == 'hungarian':
                    dist = spatial.distance_matrix(coor, coor @ rot)
                    row, col = optimize.linear_sum_assignment(dist)
                    cost[hinds, n] = dist[row, col]
                # if nodes can be assigned multiple targets, we can simply use
                # the absolute minimum of the distances (no optimization
                # required) which is _much_ lighter on memory
                # huge thanks to https://stackoverflow.com/a/47779290 for this
                # memory-efficient method
                elif method == 'original':
                    dist, col = spatial.cKDTree(coor @ rot).query(coor, 1)
                    cost[hinds, n] = dist

                resampled[hinds] = inds[hinds][col]

            # if we want to check for duplicates ensure that we don't have any
            if check_duplicates:
                if np.any(np.all(resampled[:, None] == spinsamples[:, :n], 0)):
                    duplicated = True
                # if our "spin" is identical to the input then that's no good
                elif np.all(resampled == inds):
                    duplicated = True

        # if we broke out because we tried 500 rotations and couldn't generate
        # a new one, warn that we're using duplicate rotations and give up.
        # this should only be triggered if check_duplicates is set to True
        if count == 500 and not warned:
            warnings.warn('Duplicate rotations used. Check resampling array '
                          'to determine real number of unique permutations.')
            warned = True

        spinsamples[:, n] = resampled

    if verbose:
        print(' ' * len(msg) + '\b' * len(msg), end='', flush=True)

    if return_cost:
        return spinsamples, cost

    return spinsamples


def spin_parcels(surfaces, parcellation, method='surface', n_rotate=1000,
                 spins=None, verbose=False, **kwargs):
    """
    Rotates parcels in `parcellation` and re-assigns based on maximum overlap

    Vertex labels are rotated and a new label is assigned to each *parcel*
    based on the region maximally overlapping with its boundaries.

    Parameters
    ----------
    surfaces : (2,) list-of-str
        Surfaces to use for rotating parcels; generally spherical surfaces
        are recommended. Surfaces should be (left, right) hemisphere
    parcellation : (2,) list-of-str, optional
        Path to GIFTI label files containing parcel labels on the (left, right)
        hemisphere of `surfaces`
    n_rotate : int, optional
        Number of rotations to generate. Default: 1000
    spins : array_like, optional
        Pre-computed spins to use instead of generating them on the fly. If not
        provided will use other provided parameters to create them. Default:
        None
    seed : {int, np.random.RandomState instance, None}, optional
        Seed for random number generation. Default: None
    verbose : bool, optional
        Whether to print occasional status messages. Default: False
    return_cost : bool, optional
        Whether to return cost array (specified as Euclidean distance) for each
        coordinate for each rotation. Default: True
    kwargs : key-value pairs
        Keyword arguments passed to :func:`~.gen_spinsamples`

    Returns
    -------
    spinsamples : (N, `n_rotate`) numpy.ndarray
        Resampling matrix to use in permuting data parcellated with labels from
        `parcellation`, where `N` is the number of parcels. Indices of -1
        indicate that the parcel was completely encompassed by regions in
        `drop` and should be ignored.
    """

    def overlap(vals):
        """ Returns most common positive value in `vals`; -1 if all negative
        """
        vals = np.asarray(vals)
        vals, counts = np.unique(vals[vals > 0], return_counts=True)
        try:
            return vals[counts.argmax()] - 1
        except ValueError:
            return -1

    # get vertex-level labels (set drop labels to - values)
    vertices = np.hstack([
        load_gifti(parc).agg_data() for parc in parcellation
    ])
    labels = np.unique(vertices)
    mask = labels != 0

    # get spins + cost (if requested)
    if spins is None:
        coords, hemiid = get_parcel_centroids(surfaces, method=method)
        spins = gen_spinsamples(coords, hemiid, n_rotate=n_rotate,
                                verbose=verbose, **kwargs)
        if kwargs.get('return_cost'):
            spins, cost = spins
    spins = load_spins(spins)

    if len(vertices) != len(spins):
        raise ValueError('Provided annotation files have a different '
                         'number of vertices than the specified fsaverage '
                         'surface.\n    ANNOTATION: {} vertices\n     '
                         'FSAVERAGE:  {} vertices'
                         .format(len(vertices), len(spins)))

    # spin and assign regions based on max overlap
    regions = np.zeros((len(labels[mask]), n_rotate), dtype='int32')
    for n in range(n_rotate):
        if verbose:
            msg = f'Calculating parcel overlap: {n:>5}/{n_rotate}'
            print(msg, end='\b' * len(msg), flush=True)
        regions[:, n] = labeled_comprehension(vertices[spins[:, n]], vertices,
                                              labels, overlap, int, -1)[mask]

    if kwargs.get('return_cost'):
        return regions, cost

    return regions


def parcels_to_vertices(data, parcellation):
    """
    Projects parcellated `data` to vertices as defined by `parcellation`

    Parameters
    ----------
    data : (N,) numpy.ndarray
        Parcellated data to be projected to vertices
    parcellation : tuple-of-str or os.PathLike
        Filepaths to parcellation images to project `data` to vertices

    Reurns
    ------
    projected : numpy.ndarray
        Vertex-level data
    """

    data = np.vstack(data).astype(float)
    vertices = np.hstack([
        load_gifti(parc).agg_data() for parc in parcellation
    ])
    expected = np.unique(vertices)[1:].size
    n_vert = vertices.shape[0]
    if expected != len(data):
        raise ValueError('Number of parcels in provided annotation files '
                         'differs from size of parcellated data array.\n'
                         '    EXPECTED: {} parcels\n'
                         '    RECEIVED: {} parcels'
                         .format(expected, len(data)))

    projected = np.zeros((n_vert, data.shape[-1]), dtype=data.dtype)
    n_vert = 0
    for parc in parcellation:
        labels = load_gifti(parc).agg_data().astype('int')
        currdata = np.append([[np.nan]], data, axis=0)
        projected[n_vert:n_vert + len(labels), :] = currdata[labels, :]
        n_vert += len(labels)

    return np.squeeze(projected)


def vertices_to_parcels(data, parcellation, background=None):
    """
    Reduces vertex-level `data` to parcels defined by `parcellation`.

    Compute the average `data` within each parcel. This average ignores
    vertices with background `data` values (e.g. medial wall) or with NaN
    values.

    Assigns NaN to parcels for which *all* vertices are background or NaN
    values.

    Parameters
    ----------
    data : (N,) numpy.ndarray
        Vertex-level data to be reduced to parcels
    parcellation : tuple-of-str or os.PathLike
        Filepaths to parcellation images to parcellate `data`
    background: None or float
        Specifies the background value to ignore when computing the averages.
        If None, then only vertices with NaN values are ignored. Default: None

    Returns
    ------
    reduced : numpy.ndarray
        Parcellated `data`
    """

    data = np.vstack(data)

    if background is not None:
        data[data == background] = np.nan

    vertices = np.hstack([
        load_gifti(parc).agg_data() for parc in parcellation
    ])
    n_parc = np.unique(vertices).size
    expected = vertices.shape[0]
    if expected != len(data):
        raise ValueError('Number of vertices in provided annotation files '
                         'differs from size of vertex-level data array.\n'
                         '    EXPECTED: {} vertices\n'
                         '    RECEIVED: {} vertices'
                         .format(expected, len(data)))

    numerator = np.zeros((n_parc, data.shape[-1]), dtype=data.dtype)
    denominator = np.zeros((n_parc, data.shape[-1]), dtype=data.dtype)
    start = end = 0
    for parc in parcellation:
        labels = load_gifti(parc).agg_data().astype('int')
        indices = np.unique(labels)
        end += len(labels)

        for idx in range(data.shape[-1]):
            currdata = np.squeeze(data[start:end, idx])
            counts, sums = _stats(np.nan_to_num(currdata), labels, indices)
            _, nacounts = _stats(np.isnan(currdata), labels, indices)
            counts = (np.asanyarray(counts, dtype=float)
                      - np.asanyarray(nacounts, dtype=float))

            numerator[indices, idx] += sums
            denominator[indices, idx] += counts

        start = end

    with np.errstate(divide='ignore', invalid='ignore'):
        reduced = np.squeeze(numerator / denominator)[1:]

    return reduced


def spin_data(data, surfaces, parcellation, method='surface', n_rotate=1000,
              spins=None, verbose=False, **kwargs):
    """
    Projects parcellated `data` to `surfaces`, rotates, and re-parcellates

    Projection of `data` to `surfaces` uses provided `parcellation` files.
    Re-parcellated data will not be exactly identical to original values due to
    re-averaging process. Parcels subsumed by regions in `drop` will be listed
    as NaN.

    Parameters
    ----------
    data : (N,) numpy.ndarray
        Parcellated data to be rotated. Parcels should be ordered by [left,
        right] hemisphere; ordering within hemisphere should correspond to the
        provided `parcellation` files.
    surfaces : (2,) list-of-str
        Surfaces to use for rotating parcels; generally spherical surfaces
        are recommended. Surfaces should be (left, right) hemisphere
    parcellation : (2,) list-of-str, optional
        Path to GIFTI label files containing parcel labels on the (left, right)
        hemisphere of `surfaces` mapping `data` to vertices in `surfaces`
    n_rotate : int, optional
        Number of rotations to generate. Default: 1000
    spins : array_like, optional
        Pre-computed spins to use instead of generating them on the fly. If not
        provided will use other provided parameters to create them. Default:
        None

    verbose : bool, optional
        Whether to print occasional status messages. Default: False
    kwargs : key-value pairs
        Keyword arguments passed to function used to generate rotations

    Returns
    -------
    rotated : (N, `n_rotate`) numpy.ndarray
        Rotated `data
    """

    # get coordinates and hemisphere designation for spin generation
    vertices = parcels_to_vertices(data, parcellation)

    if spins is None:
        coords, hemiid = get_parcel_centroids(surfaces, method=method)
        spins = gen_spinsamples(coords, hemiid, n_rotate=n_rotate,
                                verbose=verbose, **kwargs)
        if kwargs.get('return_cost'):
            spins, cost = spins
    spins = load_spins(spins)

    if len(vertices) != len(spins):
        raise ValueError('Provided parcellation files have a different '
                         'number of vertices than the specified surfaces.\n'
                         '    ANNOTATION: {} vertices\n'
                         '     FSAVERAGE: {} vertices'
                         .format(len(vertices), len(spins)))

    spun = np.zeros(data.shape + (n_rotate,))
    for n in range(n_rotate):
        if verbose:
            msg = f'Reducing vertices to parcels: {n:>5}/{n_rotate}'
            print(msg, end='\b' * len(msg), flush=True)
        spun[..., n] = vertices_to_parcels(vertices[spins[:, n]], parcellation)

    if verbose:
        print(' ' * len(msg) + '\b' * len(msg), end='', flush=True)

    if kwargs.get('return_cost'):
        return spun, cost

    return spun
