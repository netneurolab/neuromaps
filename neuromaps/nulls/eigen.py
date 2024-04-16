"""
helper functions for eigenstrapping null models
"""

from pathlib import Path
import warnings

import numpy as np
from eigenstrapping.base import SurfaceEigenstrapping, VolumetricEigenstrapping
from eigenstrapping.utils import eigen_decomposition, _get_eigengroups
from sklearn.utils.validation import check_random_state
from scipy.stats import special_ortho_group
from scipy.sparse import block_diag, csc_matrix
from neuromaps.datasets import fetch_atlas
from neuromaps.images import load_data,load_gifti, PARCIGNORE
try:  # scipy >= 1.8.0
    from scipy.ndimage._measurements import _stats, labeled_comprehension
except ImportError:  # scipy < 1.8.0
    from scipy.ndimage.measurements import _stats, labeled_comprehension

try:
    from joblib import Parallel, delayed
    joblib_avail = True
except ImportError:
    warnings.warn('joblib not available; cannot parallelize',
                  stacklevel=2)
    joblib_avail = False
import copy

def _vertices_to_parcels(data, parcellation=None, background=None):
    """
    Reduce vertex-level `data` to parcels defined by `parcellation`.

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
    -------
    reduced : numpy.ndarray
        Parcellated `data`
    """
    if parcellation is None:
        return data
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

def get_parcel_emodes(emodes, evals, parcellation=None,
                      atlas='fsaverage', density='10k',
                      num_modes=100):
    """
    Return masked cortical eigenmodes based on atlas values in `medials`.

    Parameters
    ----------
    emodes : (2,) list_like of str to (N/2, M) arrays
        Eigenmodes for cortical hemispheres. Eigenmodes should be (left, right)
        hemispheres
    labels : (2,) list-of-str
        Path to GIFTI or text or freesurfer annot files containing labels
        of parcels on the cortical surface for each hemisphere. Should be
        (left, right) hemisphere
    drop : list, optional
        Specifies region label in `labels` for which to drop from `emodes`.
        Default: None

    Returns
    -------
    masked : (N, M) numpy.ndarray
        Eigenmodes masked by `labels`. If `drop` is None, tries to remove
        the medial wall.
    hemiid : (N,) numpy.ndarray
        Array denoting hemisphere designation of eigenmodes in `masked`,
        where `hemiid=0` denotes the left and `hemiid=1` the right hemisphere.

    """
    if parcellation is None:
        parcellation = (None, None)
        
    if isinstance(atlas, str):
        atlas = fetch_atlas(atlas, density)
    
    masked = []
    evals_lr = []
    hemiid = []
        
    for n, (hemi, emode, parc) in enumerate(zip(['L', 'R'], emodes, parcellation)):        
        emode_hemi = _load(emode)[:, :num_modes]
        # take care of nans
        evals_hemi = np.abs(_load(evals[n])[:num_modes]) # check they aren't negative
        emode_hemi = _vertices_to_parcels(emode_hemi, parcellation=parc)
        # check if `num_modes` is not greater than number of parcels
        if num_modes >= len(emode_hemi):
            raise RuntimeError('Number of modes cannot be greater than number of parcels')
        masked.append(emode_hemi)
        evals_lr.append(evals_hemi)
        hemiid.extend([n] * emode_hemi.shape[0])
    
    return np.row_stack(masked), np.row_stack(evals_lr), np.asarray(hemiid)

def gen_eigensamples(emodes, evals, hemiid, num_modes=100, 
                     n_rotate=1000, seed=None, n_proc=1):
    """
    Return an array of rotated eigenmodes for `emodes` obtained by separate
    rotations of `n_rotate`. These are expected to be pre-masked 
    (i.e., output from `neuromaps.nulls.eigen.get_masked_emodes`).

    Parameters
    ----------
    emodes : (N, M) array_like
        Eigenmodes calculated on cortical surface for both hemispheres.
    evals : (2, M) array_like
        Eigenvalues corresponding to the eigenmodes in `emodes`. Must correspond
        to non-constant modes in ascending order.
    hemiid : (N,) array_like
        Array denoting hemisphere designation of eigenmodes in `emodes`, where
        values should be {0, 1} denoting the different hemispheres. Rotations
        are generated for one hemisphere and mirrored across the y-axis for the
        other hemisphere.
    num_modes : int, optional
        Number of eigenmodes to generate random resamples. If None, uses
        all eigenmodes in `emodes`. Default: 100
    n_rotate : int, optional
        Number of rotations to generate. Default: 1000
    seed : {int, np.random.RandomState instance, None}, optional
        Seed for reproducibility. Default: None
    verbose : bool, optional
        Whether to print status messages. Default: False
    n_proc : int, optional
        Number of processes to use while generating rotations.    
    
    Returns
    -------
    rotated_modes : (N, M, `n_rotate`) numpy.ndarray
        Rotated eigenmode matrix to use in reconstructing eigenmode surrogates.
        
    References
    ----------
    .. [ES1] Koussis, N.C., Pang, J.C., Jeganathan, J., Paton, B., 
    Fornito, A., Robinson, P.A., Misic, B., Breakspear, M. (2024). 
    Generation of surrogate brain maps preserving spatial 
    autocorrelation through random rotation of geometric eigenmodes. 
    bioRxiv 2024.02.07.579070 [Preprint]. 
    https://dx.doi.org/10.1101/2024.02.07.579070

    """
    rs = check_random_state(seed)
    hemiid = np.squeeze(np.asanyarray(hemiid, dtype='int8'))
    
    # ensure hemisphere designation array is correct
    if hemiid.ndim != 1:
        raise ValueError('Provided `hemiid` array must be one-dimensional.')
    if emodes.shape[0] != len(hemiid):
        raise ValueError('Provided `emodes` and `hemiid` must have the same '
                         'length. Provided lengths: emodes = {}, hemiid = {}'
                         .format(emodes.shape[0], len(hemiid)))
    if np.max(hemiid) > 1 or np.min(hemiid) < 0:
        raise ValueError('`hemiid` must have values in {0, 1} denoting left and '
                         'right hemisphere coordinates, respectively. '
                         + 'Provided array contains values: {}'
                         .format(np.unique(hemiid)))
    
    groups = _get_eigengroups(emodes)
    group_sizes = [len(group) for group in groups]
    seeds = rs.randint(np.iinfo(np.int32).max, size=n_rotate)
    mask = np.logical_not(np.logical_or(np.isnan(emodes[:, 0]), np.isclose(emodes[:, 0], 0)))
    rotated_modes_arr = np.zeros((len(emodes), num_modes, n_rotate)).astype(np.float32)
    
    if joblib_avail:
        spins_modes = Parallel(n_jobs=n_proc)(
            delayed(_rotation_block)(
                group_sizes, seed=seed) for seed in seeds
            )
        rotated_modes = Parallel(n_jobs=n_proc)(
            delayed(_rotate_modes)(
                emodes[mask], evals, spin, hemiid=hemiid[mask]) for spin in spins_modes
            )
        
    else:
        spins_modes = [_rotation_block(group_sizes, seed=seed) for seed in seeds]
        rotated_modes = [_rotate_modes(emodes[mask], evals, spin, hemiid=hemiid[mask]) for spin in spins_modes]
    
    rotated_modes_arr[mask] = np.stack(rotated_modes, axis=-1)
    
    return rotated_modes_arr

def _rotation_block(group_sizes, seed=None):
    """ generate block diagonal rotation matrix """
    L = np.sum(group_sizes)
    
    block_l = block_diag([_gen_rotation(group_size, seed=seed) for group_size in group_sizes], format='csc')
    # for reflecting across Y-Z plane
    reflect = np.eye(L)
    reflect[0, 0] *= -1
    
    block_r = reflect @ block_l @ reflect
    block_r = csc_matrix(block_r)
    
    return np.stack((block_l, block_r))
    
def _gen_rotation(mu, seed=None):
    """ generate random rotation for left hemisphere and reflect across Y-Z plane """
    if mu <= 1:
        return 1
    rs = check_random_state(seed)
    
    # generate rotation for left
    rotate = special_ortho_group.rvs(dim=mu, random_state=rs)
    
    return rotate

def _rotate_modes(emodes, evals, spin, hemiid):
    # rotate each hemisphere separately
    resampled = np.zeros((emodes.shape), dtype=np.single)
    for h, rot in enumerate(spin):
        hinds = (hemiid == h)
        emode = emodes[hinds]
        evals_hemi = evals[h]
        normed_emode = emode / np.sqrt(evals_hemi)
        
        # apply rotation
        resampled[hinds] = (normed_emode @ rot) * np.sqrt(evals_hemi)      
    
    return resampled  

def _load(fpattern):
    """ catch-all loading function """
    if isinstance(fpattern, np.ndarray):
        data = fpattern
    elif isinstance(fpattern, str):
        fpattern = Path(fpattern)
        fext = fpattern.suffix
        if fext == '.txt':
            try:
                data = np.loadtxt(fpattern)
            except TypeError:
                data = np.loadtxt(fpattern, delimiter=',')
        elif fext == '.gii':
            data = load_gifti(fpattern).agg_data()
            raise UserWarning('Detected gifti file. number of data arrays: {}. '
                              'please verify if this is the expected amount.'.format(str(len(data))))
        else:
            raise ValueError('Unknown file type "{}"'.format(str(fext)))
            
    return data

def eigenstrap_data(data, emodes, evals, hemiid, rotated_modes=None,
                    atlas='fsaverage', density='10k', num_modes=100, 
                    n_rotate=1000, n_proc=1, seed=None, **kwargs):
    """
    Return eigenstrapped surrogates by reconstructing `data`
    coefficients with each set of eigenmode rotations in `rotated_modes`,
    or generates eigenmode rotations on the fly if `rotated_modes` is None.

    Parameters
    ----------
    data : (N,) numpy.ndarray
        Brain maps across both hemispheres.
    emodes : (N, `num_modes`) numpy.ndarray or str
        Eigenmode set for surfaces `data` is projected or derived
    evals : (`num_modes`,) numpy.ndarray or str
        Eigenvalues corresponding to `emodes`
    parcellation : (2,) list-of-str, optional
        Path to GIFTI label files containing parcel labels on the (left, right)
        hemisphere of the surfaces `emodes` were calculated. Maps `data` from vertex
        to parcel.
    rotated_modes : (N, `num_modes`, `n_rotate`) numpy.ndarray or str-to-npy, optional
        Rotated eigenmodes generated from `gen_eigensamples` or .npy file,
        indexed by second axis across hemispheres (i.e. first `num_modes` entries
        are left hemisphere `rotated_modes`, while second `num_modes` entries
        are right hemisphere `rotated_modes`)
    num_modes : int, optional
        Number of modes to use for reconstructing data. Default: 100
    n_rotate : int, optional
        Number of rotations to generate. Default: 1000
    n_proc : int, optional
        Number of processes to use. Default: 1
    seed : int or np.random.RandomState or None, optional
        Seed for random number generation. Default: None
    kwargs : dict of key-value pairs
        Keyword arguments passed to function used to generate 
        reconstructed surrogates, e.g. {'resample' : True}

    Returns
    -------
    estrapped : (N, `n_rotate`)
        Eigenstrapping resampled data.

    """
    data = load_data(data)
    rs = check_random_state(seed)
    
    if isinstance(atlas, str):
        atlas = fetch_atlas(atlas, density)
    
    if rotated_modes is None:
        rotated_modes = gen_eigensamples(
            emodes,
            evals, 
            hemiid=hemiid,
            num_modes=num_modes,
            n_rotate=n_rotate,
            seed=rs,
            n_proc=n_proc
            )
    else:
        rotated_modes = load_rotated(rotated_modes, n_perm=n_rotate)
    
    npoints = len(data)
    mask = np.logical_not(np.logical_or(np.isnan(data), np.isclose(data, 0)))
        
    if npoints != len(rotated_modes):
        raise ValueError('Provided parcellation files have a different '
                         'number of vertices than the specified surfaces.\n'
                         '    ANNOTATION: {} vertices\n'
                         '       SURFACE: {} vertices'
                         .format(npoints, len(rotated_modes)))
    
    if n_rotate > rotated_modes.shape[-1]:
        # implement random selection of mode set
        # have a warning of how many sets were repeated
        raise NotImplementedError('Repetition of rotations is a future implementation')
        
    estrapped = np.zeros((npoints, n_rotate)) * np.nan
    estrapped_masked = []
    
    resample = False
    permute = False
    if 'resample' in kwargs:
        resample = kwargs['resample']
    if 'permute' in kwargs:
        permute = kwargs['permute']
    
    for n, hemi in enumerate(('L', 'R')):
        hinds = (hemiid[mask] == n)            
        hdata = np.squeeze(data[mask][hinds])
        hemodes = emodes[mask][hinds]
        coeffs = eigen_decomposition(hdata, hemodes)
        if joblib_avail:
            estrapped_hemi = Parallel(n_jobs=n_proc)(
                delayed(_apply_rotated)(
                    hdata, coeffs, resample, permute, seed, rotated_modes[mask][hinds, :, i]) for i in range(n_rotate)
                )
        
        else:
            estrapped_hemi = [_apply_rotated(hdata, coeffs, resample, permute, seed, rotated_modes[mask][hinds, :, i]) for i in range(n_rotate)]
            
        estrapped_masked.append(np.asarray(estrapped_hemi).T)
    
    estrapped_masked = np.row_stack(estrapped_masked)
    estrapped[mask] = estrapped_masked
    
    return estrapped

def _apply_rotated(data, coeffs, resample, permute, seed, rotated_mode):
    """ reconstructs eigenstrapping surrogates """
    rotated_data = coeffs @ rotated_mode.T
    
    if permute is True:
        rs = check_random_state(seed)
        residuals = data - rotated_data
        rotated_data += rs.permutation(residuals)
    
    if resample is True:
        data_ranks = np.argsort(data)
        np.put(rotated_data, data_ranks, data)
    else:
        rotated_data -= np.nanmean(rotated_data)
    
    return rotated_data
    
def write_rotated(filename, rotated_modes):
    """
    Write rotated eigenmodes to `writedir` as mem-mapped .npy file because BIG

    Parameters
    ----------
    filename : str-to-file
        Name of file to write rotated modes. '.npy' will be appended.
    rotated_modes : (N, M, `n_rotate`) numpy.ndarray
        Array of rotated eigenmodes.

    Returns
    -------
    fn : str-to-file
        Returns filename if successful.

    """
    if type(filename) is not str:
        raise ValueError('Input filename must be a string')
    
    fn = Path(filename)
    if fn.suffix != '.npy':
        fn = filename + '.npy'
        fn = Path(fn)
    
    if fn.exists():
        warnings.warn('rotated eigenmodes file already exists: overwriting!',
                      stacklevel=2)
     
    fnp = np.lib.format.open_memmap(
        fn, mode='w+', dtype=np.float32, shape=rotated_modes.shape)
    
    fnp[:] = rotated_modes

    del fnp    
    
    return str(fn)

def load_rotated(fn, n_perm=None):
    """
    Load spins from `fn`.

    Parameters
    ----------
    fn : os.PathLike
        Filepath to file containing spins to load
    n_perm : int, optional
        Number of rotated modes to retain (i.e., subset data)

    Returns
    -------
    rotated_modes : (N, M, `n_perm`) array_like
        Loaded rotated modes
    """
    try:
        npy = Path(fn).with_suffix('.npy')
        if npy.exists():
            rotated_modes = np.load(npy, allow_pickle=False, mmap_mode='c')
        else:
            rotated_modes = np.loadtxt(fn, delimiter=',', dtype=np.float32)
    except TypeError:
        rotated_modes = np.asarray(fn, dtype=np.float32)

    if n_perm is not None:
        rotated_modes = rotated_modes[..., :n_perm]

    return rotated_modes

# TODO volumetric eigenstrapping 
# def gen_vol_eigensamples(volumes, num_modes=100, n_rotate=1000, seed=None):
    
    
#     return rotated_modes