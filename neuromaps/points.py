# -*- coding: utf-8 -*-
"""
Functions for working with triangle meshes + surfaces
"""

from joblib import Parallel, delayed
import numpy as np
from scipy import ndimage, sparse

from neuromaps.images import load_gifti, relabel_gifti, PARCIGNORE


def point_in_triangle(point, triangle, return_pdist=True):
    """
    Checks whether `point` falls inside `triangle`

    Parameters
    ----------
    point : (3,) array_like
        Coordinates of point
    triangle (3, 3) array_like
        Coordinates of triangle
    return_pdist : bool, optional
        Whether to return planar distance (see outputs). Default: True

    Returns
    -------
    inside : bool
        Whether `point` is inside triangle
    pdist : float
        The approximate distance of the point to the plane of the triangle.
        Only returned if `return_pdist` is True
    """

    A, B, C = triangle
    v0 = C - A
    v1 = B - A
    v2 = point - A

    dot00 = np.dot(v0, v0)
    dot01 = np.dot(v0, v1)
    dot02 = np.dot(v0, v2)
    dot11 = np.dot(v1, v1)
    dot12 = np.dot(v1, v2)

    denom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * denom
    v = (dot00 * dot12 - dot01 * dot02) * denom
    inside = (u >= 0) and (v >= 0) and (u + v < 1)

    if return_pdist:
        return inside, np.abs(v2 @ np.cross(v1, v0))

    return inside


def which_triangle(point, triangles):
    """
    Determines which of `triangles` the provided `point` falls inside

    Parameters
    ----------
    point : (3,) array_like
        Coordinates of point
    triangles : (N, 3, 3) array_like
        Coordinates of `N` triangles to check

    Returns
    -------
    idx : int
        Index of `triangles` that `point` is inside of. If `point` does not
        fall within any of `triangles` then this will be None
    """

    idx, planar = None, np.inf
    for n, tri in enumerate(triangles):
        inside, pdist = point_in_triangle(point, tri)
        if pdist < planar and inside:
            idx, planar = n, pdist

    return idx


def _get_edges(faces):
    """
    Gets set of edges from `faces`

    Parameters
    ----------
    faces : (F, 3) array_like
        Set of indices creating triangular faces of a mesh

    Returns
    -------
    edges : (F*3, 2) array_like
        All edges in `faces`
    """

    faces = np.asarray(faces)
    edges = np.sort(faces[:, [0, 1, 1, 2, 2, 0]].reshape((-1, 2)), axis=1)

    return edges


def get_shared_triangles(faces):
    """
    Returns dictionary of triangles sharing edges from `faces`

    Parameters
    ----------
    faces : (N, 3)
        Triangles comprising mesh

    Returns
    -------
    shared : dict
        Where keys are len-2 tuple of vertex ids for the shared edge and values
        are the triangles that have this shared edge.
    """

    # first generate the list of edges for the provided faces and the
    # index for which face the edge is from (which is just the index of the
    # face repeated thrice, since each face generates three direct edges)
    edges = _get_edges(faces)
    edges_face = np.repeat(np.arange(len(faces)), 3)

    # every edge appears twice in a watertight surface, so we'll first get the
    # indices for each duplicate edge in `edges` (this should, assuming all
    # goes well, have rows equal to len(edges) // 2)
    order = np.lexsort(edges.T[::-1])
    edges_sorted = edges[order]
    dupe = np.any(edges_sorted[1:] != edges_sorted[:-1], axis=1)
    dupe_idx = np.append(0, np.nonzero(dupe)[0] + 1)
    start_ok = np.diff(np.concatenate((dupe_idx, [len(edges_sorted)]))) == 2
    groups = np.tile(dupe_idx[start_ok].reshape(-1, 1), 2)
    edge_groups = order[groups + np.arange(2)]

    # now, get the indices of the faces that participate in these duplicate
    # edges, as well as the edges themselves
    adjacency = edges_face[edge_groups]
    nondegenerate = adjacency[:, 0] != adjacency[:, 1]
    adjacency = np.sort(adjacency[nondegenerate], axis=1)
    adjacency_edges = edges[edge_groups[:, 0][nondegenerate]]

    # the non-shared vertex index is the same shape as adjacency, holding
    # vertex indices vs face indices
    indirect_edges = np.zeros(adjacency.shape, dtype=np.int32) - 1

    # loop through the two columns of adjacency
    for i, fid in enumerate(adjacency.T):
        # faces from the current column of adjacency
        face = faces[fid]
        # get index of vertex not included in shared edge
        unshared = np.logical_not(np.logical_or(
            face == adjacency_edges[:, 0].reshape(-1, 1),
            face == adjacency_edges[:, 1].reshape(-1, 1)))
        # each row should have one "uncontained" vertex; ignore degenerates
        row_ok = unshared.sum(axis=1) == 1
        unshared[~row_ok, :] = False
        indirect_edges[row_ok, i] = face[unshared]

    # get vertex coordinates of triangles pairs with shared edges, ordered
    # such that the non-shared vertex is always _last_ among the trio
    shared = np.sort(face[np.logical_not(unshared)].reshape(-1, 1, 2), axis=-1)
    shared = np.repeat(shared, 2, axis=1)
    triangles = np.concatenate((shared, indirect_edges[..., None]), axis=-1)

    return dict(zip(map(tuple, adjacency_edges), triangles))


def get_direct_edges(vertices, faces):
    """
    Gets (unique) direct edges and weights in mesh describes by inputs.

    Parameters
    ----------
    vertices : (N, 3) array_like
        Coordinates of `vertices` comprising mesh with `faces`
    faces : (F, 3) array_like
        Indices of `vertices` that compose triangular faces of mesh

    Returns
    -------
    edges : (E, 2) array_like
        Indices of `vertices` comprising direct edges (without duplicates)
    weights : (E, 1) array_like
        Distances between `edges`
    """

    edges = np.unique(_get_edges(faces), axis=0)
    weights = np.linalg.norm(np.diff(vertices[edges], axis=1), axis=-1)
    return edges, weights.squeeze()


def get_indirect_edges(vertices, faces):
    """
    Gets indirect edges and weights in mesh described by inputs

    Indirect edges are between two vertices that participate in faces sharing
    an edge

    Parameters
    ----------
    vertices : (N, 3) array_like
        Coordinates of `vertices` comprising mesh with `faces`
    faces : (F, 3) array_like
        Indices of `vertices` that compose triangular faces of mesh

    Returns
    -------
    edges : (E, 2) array_like
        Indices of `vertices` comprising indirect edges (without duplicates)
    weights : (E, 1) array_like
        Distances between `edges` on surface

    References
    ----------
    https://github.com/mikedh/trimesh (MIT licensed)
    """

    triangles = np.stack(list(get_shared_triangles(faces).values()), axis=0)
    indirect_edges = triangles[..., -1]

    # `A.shape`: (3, N, 2) corresponding to (xyz coords, edges, triangle pairs)
    A, B, V = vertices[triangles].transpose(2, 3, 0, 1)

    # calculate the xyz coordinates of the foot of each triangle, where the
    # base is the shared edge
    # that is, we're trying to calculate F in the equation `VF = VB - (w * BA)`
    # where `VF`, `VB`, and `BA` are vectors, and `w = (AB * VB) / (AB ** 2)`
    w = (np.sum((A - B) * (V - B), axis=0, keepdims=True)
         / np.sum((A - B) ** 2, axis=0, keepdims=True))
    feet = B - (w * (B - A))
    # calculate coordinates of midpoint b/w the feet of each pair of triangles
    midpoints = (np.sum(feet.transpose(1, 2, 0), axis=1) / 2)[:, None]
    # calculate Euclidean distance between non-shared vertices and midpoints
    # and add distances together for each pair of triangles
    norms = np.linalg.norm(vertices[indirect_edges] - midpoints, axis=-1)
    weights = np.sum(norms, axis=-1)

    # NOTE: weights won't be perfectly accurate for a small subset of triangle
    # pairs where either triangle has angle >90 along the shared edge. in these
    # the midpoint lies _outside_ the shared edge, so neighboring triangles
    # would need to be taken into account. that said, this occurs in only a
    # minority of cases and the difference tends to be in the ~0.001 mm range
    return indirect_edges, weights


def make_surf_graph(vertices, faces, mask=None):
    """
    Constructs adjacency graph from `surf`.

    Parameters
    ----------
    vertices : (N, 3) array_like
        Coordinates of `vertices` comprising mesh with `faces`
    faces : (F, 3) array_like
        Indices of `vertices` that compose triangular faces of mesh
    mask : (N,) array_like, optional (default None)
        Boolean mask indicating which vertices should be removed from generated
        graph. If not supplied, all vertices are used.

    Returns
    -------
    graph : scipy.sparse.csr_matrix
        Sparse matrix representing graph of `vertices` and `faces`

    Raises
    ------
    ValueError
        Inconsistent number of vertices in `mask` and `vertices`
    """

    if mask is not None and len(mask) != len(vertices):
        raise ValueError('Supplied `mask` array has different number of '
                         'vertices than supplied `vertices`.')

    # get all (direct + indirect) edges from surface
    direct_edges, direct_weights = get_direct_edges(vertices, faces)
    indirect_edges, indirect_weights = get_indirect_edges(vertices, faces)
    edges = np.row_stack((direct_edges, indirect_edges))
    weights = np.hstack((direct_weights, indirect_weights))

    # remove edges that include a vertex in `mask`
    if mask is not None:
        idx, = np.where(mask)
        mask = ~np.any(np.isin(edges, idx), axis=1)
        edges, weights = edges[mask], weights[mask]

    # construct our graph on which to calculate shortest paths
    return sparse.csr_matrix((np.squeeze(weights), (edges[:, 0], edges[:, 1])),
                             shape=(len(vertices), len(vertices)))


def _get_graph_distance(vertex, graph, labels=None):
    """
    Gets surface distance of `vertex` to all other vertices in `graph`

    Parameters
    ----------
    vertex : int
        Index of vertex for which to calculate surface distance
    graph : array_like
        Graph along which to calculate shortest path distances
    labels : array_like, optional
        Labels indicating parcel to which each vertex belongs. If provided,
        distances will be averaged within distinct labels

    Returns
    -------
    dist : (N,) numpy.ndarray
        Distance of `vertex` to all other vertices in `graph` (or to all
        parcels in `labels`, if provided)
    """

    dist = sparse.csgraph.dijkstra(graph, directed=False, indices=[vertex])

    if labels is not None:
        dist = ndimage.mean(input=np.delete(dist, vertex),
                            labels=np.delete(labels, vertex),
                            index=np.unique(labels))

    return dist.astype('float32')


def get_surface_distance(surface, parcellation=None, medial=None,
                         medial_labels=None, drop=None, n_proc=1):
    """
    Calculates surface distance for vertices in `surface`

    Parameters
    ----------
    surface : str or os.PathLike
        Path to surface file on which to calculate distance
    parcellation : str or os.PathLike, optional
        Path to file with parcel labels for provided `surface`. If provided
        will calculate parcel-parcel distances instead of vertex distances,
        where parcel-parcel distance is the average distance between all
        constituent vertices in two parcels. Default: None
    medial : str or os.PathLike, optional
        Path to file indicating which vertices correspond to the medial wall
        (0 indicates medial wall). If provided will prohibit calculation of
        surface distance along the medial wall. Superseded by `medial_labels`
        if both are provided. Default: None
    medial_labels : list of str, optional
        List of parcel names that comprise the medial wall and through which
        travel should be disallowed. Only valid if `parcellation` is provided;
        supersedes `medial` if both are provided. Default: None
    drop : list of str, optional
        List of parcel names that should be dropped from the final distance
        matrix (if `parcellation` is provided). If not specified, will ignore
        parcels commonly used to reference the medial wall (e.g., 'unknown',
        'corpuscallosum', '???', 'Background+FreeSurfer_Defined_Medial_Wall').
        Default: None
    n_proc : int, optional
        Number of processors to use for parallelizing distance calculation. If
        negative, will use max available processors plus 1 minus the specified
        number. Default: 1 (no parallelization)

    Returns
    -------
    distance : (N, N) numpy.ndarray
        Surface distance between vertices/parcels on `surface`
    """

    if drop is None:
        drop = PARCIGNORE

    if medial_labels is not None:
        if isinstance(medial_labels, str):
            medial_labels = [medial_labels]
        drop = set(drop + list(medial_labels))

    vert, faces = load_gifti(surface).agg_data()
    n_vert = vert.shape[0]
    labels, mask = None, np.zeros(n_vert, dtype=bool)

    # get data from parcellation / medial wall files if provided
    if medial is not None:
        mask = np.logical_not(load_gifti(medial).agg_data().astype(bool))
    if parcellation is not None:
        parcellation, = relabel_gifti(parcellation, background=drop)
        labels = load_gifti(parcellation).agg_data()
        mask[labels == 0] = True

    # calculate distance from each vertex to all other vertices
    graph = make_surf_graph(vert, faces, mask=mask)
    dist = np.row_stack(Parallel(n_jobs=n_proc, max_nbytes=None)(
        delayed(_get_graph_distance)(n, graph, labels) for n in range(n_vert)
    ))

    # average distance for all vertices within a parcel + set diagonal to 0
    if labels is not None:
        dist = np.row_stack([
            dist[labels == lab].mean(axis=0) for lab in np.unique(labels)
        ])
        dist[np.diag_indices_from(dist)] = 0
        dist = dist[1:, 1:]

    # remove distances for parcels that we aren't interested in
    return dist


def _geodesic_parcel_centroid(vertices, faces, inds):
    """
    Calculates parcel centroids based on surface distance

    Parameters
    ----------
    vertices : (N, 3)
        Coordinates of vertices defining surface
    faces : (F, 3)
        Triangular faces defining surface
    inds : (R,)
        Indices of `vertices` that belong to parcel

    Returns
    --------
    roi : (3,) numpy.ndarray
        Vertex corresponding to centroid of parcel
    """

    mask = np.ones(len(vertices), dtype=bool)
    mask[inds] = False
    mat = make_surf_graph(vertices, faces, mask=mask)
    paths = sparse.csgraph.dijkstra(mat, directed=False, indices=inds)[:, inds]

    # the selected vertex is the one with the minimum average shortest path
    # to the other vertices in the parcel
    roi = vertices[inds[paths.mean(axis=1).argmin()]]

    return roi
