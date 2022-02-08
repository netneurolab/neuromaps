# -*- coding: utf-8 -*-
"""
Functions for fetching datasets (from the internet, if necessary)
"""

from collections import namedtuple
import os
from pathlib import Path

from nilearn.datasets.utils import _fetch_files
from sklearn.utils import Bunch

from neuromaps.datasets.utils import get_data_dir, get_dataset_info

SURFACE = namedtuple('Surface', ('L', 'R'))
ALIAS = dict(
    fslr='fsLR', fsavg='fsaverage', mni152='MNI152', mni='MNI152',
    FSLR='fsLR', CIVET='civet'
)
DENSITIES = dict(
    civet=['41k', '164k'],
    fsaverage=['3k', '10k', '41k', '164k'],
    fsLR=['4k', '8k', '32k', '164k'],
    MNI152=['1mm', '2mm', '3mm'],
)


_atlas_docs = dict(
    url="""\
url : str, optional
    URL from which to download data. Default: None\
""",
    data_dir="""\
data_dir : str, optional
    Path to use as data directory. If not specified, will check for
    environmental variable 'neuromaps_DATA'; if that is not set, will
    use `~/neuromaps-data` instead. Default: None\
""",
    verbose="""\
verbose : int, optional
    Modifies verbosity of download, where higher numbers mean more updates.
    Default: 1\
""",
    genericatlas="""\
atlas : dict
    Dictionary where keys are atlas types and values are atlas files\
""",
    surfatlas="""\
atlas : dict
    Dictionary where keys are atlas types and values are tuples of atlas
    files (L/R hemisphere)\
"""
)


def _sanitize_atlas(atlas):
    """ Checks for aliases of `atlas` and confirms valid input
    """
    atlas = ALIAS.get(atlas, atlas)
    if atlas not in DENSITIES:
        raise ValueError(f'Invalid atlas: {atlas}.')
    return atlas


def _bunch_outputs(keys, values, surface=True):
    """ Groups `values` together (L/R) if `surface` and zips with `keys`
    """
    if surface:
        values = [SURFACE(*values[i:i + 2]) for i in range(0, len(values), 2)]
    return Bunch(**dict(zip(keys, values)))


def _fetch_atlas(atlas, density, keys, url=None, data_dir=None, verbose=1):
    """ Helper function to get requested `atlas`
    """

    atlas = _sanitize_atlas(atlas)
    densities = DENSITIES[atlas]
    if density not in densities:
        raise ValueError(f'Invalid density: {density}. Must be one of '
                         f'{densities}')

    data_dir = get_data_dir(data_dir=data_dir)
    info = get_dataset_info(atlas)[density]
    if url is None:
        url = info['url']
    opts = {
        'uncompress': True,
        'md5sum': info['md5'],
        'move': f'{atlas}{density}.tar.gz'
    }

    if atlas == 'MNI152':
        filenames = [
            f'tpl-MNI152NLin2009cAsym_res-{density}{suff}.nii.gz'
            for suff in ('_T1w', '_T2w', '_PD', '_desc-brain_mask',
                         '_label-csf_probseg', '_label-gm_probseg',
                         '_label-wm_probseg')
        ]
        if density in ('1mm', '2mm'):
            filenames += [
                f'tpl-MNI152NLin6Asym_res-{density}{suff}.nii.gz'
                for suff in ('_T1w', '_desc-brain_mask')
            ]

    else:
        filenames = [
            'tpl-{}_den-{}_hemi-{}_{}.surf.gii'
            .format(atlas, density, hemi, surf)
            for surf in keys
            for hemi in ('L', 'R')
        ] + [
            'tpl-{}_den-{}_hemi-{}_desc-{}.gii'
            .format(atlas, density, hemi, desc)
            for desc in ('nomedialwall_dparc.label',
                         'sulc_midthickness.shape',
                         'vaavg_midthickness.shape')
            for hemi in ('L', 'R')
        ]
        keys += ['medial', 'sulc', 'vaavg']

    filenames = [os.path.join('atlases', atlas, fn) for fn in filenames]
    data = [
        Path(fn) for fn in
        _fetch_files(data_dir, files=[(f, url, opts) for f in filenames],
                     verbose=verbose)
    ]

    return _bunch_outputs(keys, data, atlas != 'MNI152')


def fetch_civet(density='41k', url=None, data_dir=None, verbose=1):
    keys = ['white', 'midthickness', 'inflated', 'veryinflated', 'sphere']
    return _fetch_atlas(
        'civet', density, keys, url=url, data_dir=data_dir, verbose=verbose
    )


fetch_civet.__doc__ = """
Fetches CIVET surface atlas

Parameters
----------
density : {{'{densities}'}}, optional
    Density of CIVET atlas to fetch. Default: '41k'
{url}
{data_dir}
{verbose}

Returns
-------
{surfatlas}
""".format(**_atlas_docs, densities="', '".join(DENSITIES['civet']))


def fetch_fsaverage(density='41k', url=None, data_dir=None, verbose=1):
    keys = ['white', 'pial', 'inflated', 'sphere']
    return _fetch_atlas(
        'fsaverage', density, keys, url=url, data_dir=data_dir, verbose=verbose
    )


fetch_fsaverage.__doc__ = """
Fetches fsaverage surface atlas

Parameters
----------
density : {{'{densities}'}}, optional
    Density of fsaverage atlas to fetch. Default: '41k'
{url}
{data_dir}
{verbose}

Returns
-------
{surfatlas}
""".format(**_atlas_docs, densities="', '".join(DENSITIES['fsaverage']))


def fetch_fslr(density='32k', url=None, data_dir=None, verbose=1):
    keys = ['midthickness', 'inflated', 'veryinflated', 'sphere']
    if density in ('4k', '8k'):
        keys.remove('veryinflated')
    return _fetch_atlas(
        'fsLR', density, keys, url=url, data_dir=data_dir, verbose=verbose
    )


fetch_fslr.__doc__ = """
Fetches fsLR surface atlas

Parameters
----------
density : {{'{densities}'}}, optional
    Density of fsLR atlas to fetch. Default: '32k'
{url}
{data_dir}
{verbose}

Returns
-------
{surfatlas}
""".format(**_atlas_docs, densities="', '".join(DENSITIES['fsLR']))


def fetch_mni152(density='1mm', url=None, data_dir=None, verbose=1):
    keys = ['2009cAsym_T1w', '2009cAsym_T2w', '2009cAsym_PD',
            '2009cAsym_brainmask', '2009cAsym_CSF', '2009cAsym_GM',
            '2009cAsym_WM']
    if density in ('1mm', '2mm'):
        keys += ['6Asym_T1w', '6Asym_brainmask']
    return _fetch_atlas(
        'MNI152', density, keys, url=url, data_dir=data_dir, verbose=verbose
    )


fetch_mni152.__doc__ = """
Fetches MNI152 atlas

Parameters
----------
density : {{'{densities}'}}, optional
    Resolution of MNI152 atlas to fetch. Default: '1mm'
{url}
{data_dir}
{verbose}

Returns
-------
{genericatlas}
""".format(**_atlas_docs, densities="', '".join(DENSITIES['MNI152']))


def fetch_regfusion(atlas, url=None, data_dir=None, verbose=1):
    atlas = _sanitize_atlas(atlas)
    densities = DENSITIES[atlas].copy()
    invalid = dict(civet=('164k',), fsLR=('4k', '8k'))
    for remove in invalid.get(atlas, []):
        densities.remove(remove)

    data_dir = get_data_dir(data_dir=data_dir)
    info = get_dataset_info('regfusion')
    if url is None:
        url = info['url']
    opts = {
        'uncompress': True,
        'md5sum': info['md5'],
        'move': 'regfusion.tar.gz'
    }

    filenames = [
        'tpl-MNI152_space-{}_den-{}_hemi-{}_regfusion.txt'
        .format(atlas, density, hemi)
        for density in densities
        for hemi in ['L', 'R']
    ]
    filenames = [os.path.join('atlases', 'regfusion', fn) for fn in filenames]

    data = [
        Path(fn) for fn in
        _fetch_files(data_dir, files=[(f, url, opts) for f in filenames],
                     verbose=verbose)
    ]
    return _bunch_outputs(densities, data)


fetch_regfusion.__doc__ = """
Fetches regfusion inputs for mapping MNI152 to specified surface `atlas`

Parameters
----------
atlas : {{'civet', 'fsaverage', 'fsLR'}}
    Atlas to fetch
{url}
{data_dir}
{verbose}

Returns
-------
regfusion : dict
    Dictionary where keys are surface densities and values are regfusion inputs
""".format(**_atlas_docs)


def fetch_atlas(atlas, density, url=None, data_dir=None, verbose=1):
    atlas = _sanitize_atlas(atlas)
    fetcher = globals()[f'fetch_{atlas.lower()}']
    return fetcher(density, url=url, data_dir=data_dir, verbose=verbose)


fetch_atlas.__doc__ = """
Fetches specified `atlas` and `density`

Parameters
----------
atlas : {{'{atlases}'}}
    Atlas to fetch
density : str
    Density (or resolution) of `atlas`. Must be valid for provided `atlas`
{url}
{data_dir}
{verbose}

Returns
-------
{genericatlas}
""".format(**_atlas_docs, atlases="', '".join(DENSITIES.keys()))


def fetch_all_atlases(data_dir=None, verbose=1):
    atlases = {'regfusion': {}}
    for key, resolutions in DENSITIES.items():
        atlases[key] = {}
        for res in resolutions:
            atlases[key][res] = \
                fetch_atlas(key, res, data_dir=data_dir, verbose=verbose)
        if key != 'MNI152':
            atlases['regfusion'][key] = \
                fetch_regfusion(key, data_dir=data_dir, verbose=verbose)

    return atlases


fetch_all_atlases.__doc__ = """
Fetches (and caches) all available atlases

Parameters
----------
{data_dir}
{verbose}

Returns
-------
atlases : dict
    Nested dictionaries containing all available atlases
"""


def get_atlas_dir(atlas, data_dir=None):
    try:
        atlas = _sanitize_atlas(atlas)
    except ValueError as err:
        if atlas != 'regfusion':
            raise err
    return Path(get_data_dir(data_dir=data_dir)) / 'atlases' / atlas


get_atlas_dir.__doc__ = """
Returns filepath to specified `atlas`

Parameters
----------
atlas : str
    Atlas for which filepath should be returned
{data_dir}

Returns
-------
atlas_dir : os.PathLike
    Full filepath to `atlas` directory

Raises
------
ValueError
    If provided `atlas` is not valid
""".format(**_atlas_docs)
