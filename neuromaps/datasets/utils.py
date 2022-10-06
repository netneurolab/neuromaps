# -*- coding: utf-8 -*-
"""Utilities for loading / creating datasets."""

import json
import os
from pkg_resources import resource_filename
from nilearn.datasets.utils import _md5_sum_file
import requests

# osf repo prefix
RESTRICTED = ["grh4d"]

# uniquely identify each item ('hemi' can be None)
FNAME_SURF_KEYS = ['source', 'desc', 'space', 'den', 'hemi']
FNAME_VOL_KEYS = ['source', 'desc', 'space', 'res']
# auto-generated (checksum can be None if file doest not exist)
AUTO_KEYS = ['format', 'fname', 'rel_path', 'checksum']
# required keys but values are all optional
COND_KEYS = ['title', 'tags', 'redir', 'url']
# keys for more metadata in info.json
INFO_KEYS = ['annot', 'full_desc', 'refs', 'demographics']
INFO_REFS_KEYS = ['primary', 'secondary']
INFO_DEMO_KEYS = ['N', 'age']


def _osfify_urls(data, return_restricted=True):
    """
    Format `data` object with OSF API URL.

    Parameters
    ----------
    data : object
        If dict with a `url` key, will format OSF_API with relevant values
    return_restricted : bool, optional
        Whether to return restricted annotations. These will only be accessible
        with a valid OSF token. Default: True

    Returns
    -------
    data : object
        Input data with all `url` dict keys formatted
    """
    OSF_API = "https://files.osf.io/v1/resources/{}/providers/osfstorage/{}"

    if isinstance(data, str) or data is None:
        return data
    elif 'url' in data:
        # if url is None then we this is a malformed entry and we should ignore
        if data['url'] is None:
            return
        # if the url isn't a string assume we're supposed to format it
        elif not isinstance(data['url'], str):
            if data['url'][0] in RESTRICTED and not return_restricted:
                return
            data['url'] = OSF_API.format(*data['url'])

    try:
        for key, value in data.items():
            data[key] = _osfify_urls(value, return_restricted)
    except AttributeError:
        for n, value in enumerate(data):
            data[n] = _osfify_urls(value, return_restricted)
        # drop the invalid entries
        data = [d for d in data if d is not None]

    return data


def get_dataset_info(name, return_restricted=True):
    """
    Return information for requested dataset `name`.

    Parameters
    ----------
    name : str
        Name of dataset
    return_restricted : bool, optional
        Whether to return restricted annotations. These will only be accessible
        with a valid OSF token. Default: True

    Returns
    -------
    dataset : dict or list-of-dict
        Information on requested data
    """
    fn = resource_filename('neuromaps',
                           os.path.join('datasets', 'data', 'osf.json'))
    with open(fn) as src:
        osf_resources = _osfify_urls(json.load(src), return_restricted)

    try:
        resource = osf_resources[name]
    except KeyError:
        raise KeyError("Provided dataset '{}' is not valid. Must be one of: {}"
                       .format(name, sorted(osf_resources.keys()))) from None

    return resource


def get_data_dir(data_dir=None):
    """
    Get path to neuromaps data directory.

    Parameters
    ----------
    data_dir : str, optional
        Path to use as data directory. If not specified, will check for
        environmental variable 'NEUROMAPS_DATA'; if that is not set, will
        use `~/neuromaps-data` instead. Default: None

    Returns
    -------
    data_dir : str
        Path to use as data directory
    """
    if data_dir is None:
        data_dir = os.environ.get('NEUROMAPS_DATA',
                                  os.path.join('~', 'neuromaps-data'))
    data_dir = os.path.expanduser(data_dir)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    return data_dir


def _get_token(token=None):
    """
    Return `token` if provided or set as environmental variable.

    Parameters
    ----------
    token : str, optional
        OSF personal access token for accessing restricted annotations. Will
        also check the environmental variable 'NEUROMAPS_OSF_TOKEN' if not
        provided; if that is not set no token will be provided and restricted
        annotations will be inaccessible. Default: None

    Returns
    -------
    token : str
        OSF token
    """
    if token is None:
        token = os.environ.get('NEUROMAPS_OSF_TOKEN', None)

    return token


def _get_session(token=None):
    """
    Return requests.Session with `token` auth in header if supplied.

    Parameters
    ----------
    token : str, optional
        OSF personal access token for accessing restricted annotations. Will
        also check the environmental variable 'NEUROMAPS_OSF_TOKEN' if not
        provided; if that is not set no token will be provided and restricted
        annotations will be inaccessible. Default: None

    Returns
    -------
    session : requests.Session
        Session instance with authentication in header
    """
    session = requests.Session()
    token = _get_token(token)
    if token is not None:
        session.headers['Authorization'] = 'Bearer {}'.format(token)

    return session


def parse_filename(fname, return_ext=True, verbose=False):
    """
    Parses `fname` (in BIDS-inspired format) and returns dictionary

    Parameters
    ----------
    fname : str os os.PathLike
        Filename to parse
    return_ext : bool, optional
        Whether to return extension of `fname` in addition to key-value dict.
        Default: False
    verbose : bool, optional
        Whether to print status messages. Default: False

    Returns
    -------
    info : dict
        Key-value pairs extracted from `fname`
    ext : str
        Extension of `fname`, only returned if `return_ext=True`
    """

    try:
        base, *ext = fname.split('.')
        fname_dict = dict([
            pair.split('-') for pair in base.split('_') if pair != 'feature'
        ])
    except ValueError:
        print('Wrong filename format!')
        return

    if verbose:
        print(fname_dict)

    if return_ext:
        return fname_dict, '.'.join(ext)

    return fname_dict


def parse_fname_list(fname, verbose=False):
    """
    Reads in list of BIDS-inspired filenames from `fname` and parses keys

    Parameters
    ----------
    fname : str os os.PathLike
    verbose : bool, optional
        Whether to print status messages. Default: False

    Returns
    -------
    data : list-of-dict
        Information about filenames in `fname`
    """

    with open(fname, 'r', encoding='utf-8') as src:
        fname_list = [name.strip() for name in src.readlines()]
    data = [
        parse_filename(name, return_ext=False, verbose=verbose)
        for name in fname_list
    ]
    if verbose:
        print(fname_list)

    return data


def parse_json(fname, root='annotations'):
    """
    Loads JSON from `fname` and returns value of `root` key(s)

    Parameters
    ----------
    fname : str or os.PathLike
        Filepath to JSON file
    root : str or list-of-str, optional
        Root key(s) to query JSON file. Default: 'annotations'

    Returns
    -------
    data : dict
        Data from `fname` JSON file
    """

    if isinstance(root, str):
        root = [root]

    with open(fname, 'r', encoding='utf-8') as src:
        data = json.load(src)

    for key in root:
        data = data[key]

    return data


def generate_auto_keys(data_dict, file_path=None):
    """
    Adds automatically-generated keys to `item`

    Generated keys include: ['format', 'fname', 'rel_path', 'checksum']
    Supposedly this function will fill these keys, however, if file_path
    is not give, 'checksum' will be None. The 'format' key can also be
    pre-given.

    Parameters
    ----------
    data_dict : dict
        Dict about annotation
    file_path : str or os.PathLike, optional
        Full path to file to generate checksum for. Default: None

    Returns
    -------
    item : dict
        Updated dict about annotation
    """

    item = data_dict.copy()

    pref = 'source-{source}_desc-{desc}_space-{space}'
    surffmt = pref + '_den-{den}_hemi-{hemi}_feature.func.gii'
    volfmt = pref + '_res-{res}_feature.nii.gz'

    # 'format' and 'fname'
    if ('den' in data_dict or 'hemi' in data_dict) and 'res' not in data_dict:
        item['format'] = 'surface'
        item['fname'] = surffmt.format(**item)
    elif 'res' in data_dict and \
         'den' not in data_dict and \
         'hemi' not in data_dict:
        item['format'] = 'volume'
        item['fname'] = volfmt.format(**item)
    else:
        raise ValueError('Wrong data_dict keys passed: '
                         'conflicts in file format.')

    # 'rel_path'
    item['rel_path'] = os.path.join(*[
        item[key] for key in ['source', 'desc', 'space']
    ])

    # 'checksum', optionally
    if file_path is not None and os.path.isfile(file_path):
        item['checksum'] = _md5_sum_file(file_path)
    else:
        item['checksum'] = None

    return item


def clean_contrib_keys(info, file_path=None):
    """
    Cleans contributor keys in `info` dictionary for the contribution pipeline

    Parameters
    ----------
    info : dict
        Dict about annotation
    file_path : str or os.PathLike, optional
        Full path to file to generate checksum for. Default: None

    Returns
    -------
    output : dict
        Updated dict about annotation
    """
    if 'den' in info:
        curr_keys = FNAME_SURF_KEYS + AUTO_KEYS + COND_KEYS
    elif 'res' in info:
        curr_keys = FNAME_VOL_KEYS + AUTO_KEYS + COND_KEYS
    else:
        raise ValueError('Error in input info dict')

    output = {key: (info[key] if key in info else None) for key in curr_keys}

    output = generate_auto_keys(output, file_path)

    return output
