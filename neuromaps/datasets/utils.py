# -*- coding: utf-8 -*-
"""Utilities for loading / creating datasets."""

import json
import os
import importlib.resources
import requests

# osf repo prefix
RESTRICTED = ["grh4d"]

# uniquely identify each item ('hemi' can be None)
FNAME_SURF_KEYS = ['source', 'desc', 'space', 'den', 'hemi']
FNAME_VOL_KEYS = ['source', 'desc', 'space', 'res']
# auto-generated (checksum can be None if file doesn't not exist)
AUTO_KEYS = ['format', 'fname', 'rel_path', 'checksum']
# required keys but values are all optional
COND_KEYS = ['title', 'tags', 'redir', 'url']
# keys for more metadata in info.json
INFO_KEYS = ['annot', 'full_desc', 'refs', 'demographics']
INFO_REFS_KEYS = ['primary', 'secondary']
INFO_DEMO_KEYS = ['N', 'age']


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


def _load_resource_json(relative_path):
    """
    Load JSON file from package resources.

    Parameters
    ----------
    relative_path : str
        Path to JSON file relative to package resources

    Returns
    -------
    resource_json : dict
        JSON file loaded as a dictionary
    """
    # handling pkg_resources.resource_filename deprecation
    if getattr(importlib.resources, 'files', None) is not None:
        f_resource = importlib.resources.files("neuromaps") / relative_path
    else:
        from pkg_resources import resource_filename
        f_resource = resource_filename('neuromaps', relative_path)

    with open(f_resource) as src:
        resource_json = json.load(src)

    return resource_json


NEUROMAPS_DATASETS = _load_resource_json('datasets/data/osf.json')
NEUROMAPS_DATASETS = _osfify_urls(NEUROMAPS_DATASETS, return_restricted=True)
NEUROMAPS_DATASETS_PUBLIC = _osfify_urls(NEUROMAPS_DATASETS, return_restricted=False)


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
    try:
        if return_restricted:
            return NEUROMAPS_DATASETS[name]
        else:
            return NEUROMAPS_DATASETS_PUBLIC[name]
    except KeyError:
        raise KeyError(
            f"Provided dataset '{name}' is not valid. "
            f"Must be one of: {sorted(NEUROMAPS_DATASETS.keys())}"
        ) from None


NEUROMAPS_META = _load_resource_json('datasets/data/meta.json')


def get_meta_info(name):
    """
    Return metadata for requested dataset `name`.

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
    try:
        return NEUROMAPS_META[name]
    except KeyError:
        raise KeyError(
            f"Provided dataset '{name}' is not valid. "
            f"Must be one of: {sorted(NEUROMAPS_META.keys())}"
        ) from None


def get_references(name, verbose=1, return_dict=False):
    """
    Return reference information for dataset `name`.

    Parameters
    ----------
    name : str
        Name of dataset

    Returns
    -------
    reference : str
        Reference information for dataset
    """
    pass
    # try:
    #     curr_refs = NNT_REFERENCES[name]
    #     if verbose:
    #         print("Please cite the following papers if you are using this function:")
    #         for bib_category, bib_category_items in curr_refs.items():
    #             print(f"  [{bib_category}]:")
    #             for bib_item in bib_category_items:
    #                 print(f"    {bib_item['citation']}")

    #     if return_dict:
    #         return curr_refs

    # except KeyError:
    #     raise KeyError("Provided dataset '{}' is not valid. Must be one of: {}"
    #                    .format(name, sorted(NNT_REFERENCES.keys()))) from None


def parse_filename(fname, return_ext=True, verbose=False):
    """
    Parse `fname` (in BIDS-inspired format) and returns dictionary.

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
    Read in list of BIDS-inspired filenames from `fname` and parses keys.

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
    Load JSON from `fname` and returns value of `root` key(s).

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


def _get_osf_url(fname, project, token=None):
    """
    Get OSF API URL path for `fname` in `project`.

    Parameters
    ----------
    fname : str
        Filepath as it exists on OSF
    project : str
        Project ID on OSF
    token : str, optional
        OSF personal access token for accessing restricted annotations. Will
        also check the environmental variable 'NEUROMAPS_OSF_TOKEN' if not
        provided; if that is not set no token will be provided and restricted
        annotations will be inaccessible. Default: None

    Returns
    -------
    path : str
        Path to `fname` on OSF project `project`
    """
    url = f'https://files.osf.io/v1/resources/{project}/providers/osfstorage/'
    session = _get_session(token=token)
    path = ''
    for pathpart in fname.strip('/').split('/'):
        out = session.get(url + path)
        out.raise_for_status()
        for item in out.json()['data']:
            if item['attributes']['name'] == pathpart:
                break
        path = item['attributes']['path'][1:]

    return path


def _check_meta_json():
    """
    Check for errors in meta.json.

    For internal use only.

    Returns
    -------
    None
    """
    # reload the datasets and meta json files
    NEUROMAPS_DATASETS = _load_resource_json('datasets/data/osf.json')
    NEUROMAPS_DATASETS = _osfify_urls(NEUROMAPS_DATASETS, return_restricted=True)
    NEUROMAPS_META = _load_resource_json('datasets/data/meta.json')

    for entry in NEUROMAPS_DATASETS["annotations"]:
        # get unique identifier for each entry
        if entry["format"] == "volume":
            meta_id = {k: entry[k] for k in ['source', 'desc', 'space', 'res']}
        elif entry["format"] == "surface":
            meta_id = {k: entry[k] for k in ['source', 'desc', 'space', 'den']}
        else:
            raise ValueError(f"Invalid format for entry: {entry}")
        # check existence in meta.json
        print("Checking for missing metadata entries...")
        for meta_entry in NEUROMAPS_META["annotations"]:
            if meta_id == meta_entry["annot"]:
                break
        else:
            print(f"Missing metadata for {meta_id}")


def _fill_meta_json_refs(bib_file, json_file, overwrite=False, use_defaults=False):
    """
    Fill in citation information for references in a JSON file.

    For internal use only.

    Parameters
    ----------
    bib_file : str
        Path to BibTeX file containing references
    json_file : str
        Path to JSON file containing references
    overwrite : bool, optional
        Whether to overwrite existing citation information. Default: False
    use_defaults : bool, optional
        Whether to use default paths for `bib_file` and `json_file`. Default: False

    Returns
    -------
    None
    """
    if use_defaults:
        bib_file = \
            importlib.resources.files("neuromaps") / "datasets/data/neuromaps.bib"
        json_file = \
            importlib.resources.files("neuromaps") / "datasets/data/meta.json"

    from pybtex import PybtexEngine
    engine = PybtexEngine()

    def _get_citation(key):
        s = engine.format_from_file(
            filename=bib_file, style="unsrt",
            citations=[key], output_backend="plaintext"
            )
        return s.strip("\n").replace("[1] ", "")

    with open(json_file) as src:
        nm_meta = json.load(src)

    for entry in nm_meta["annotations"]:
        for bib_category in ["primary", "secondary"]:
            for bib_item in entry["refs"][bib_category]:
                if bib_item["bibkey"] not in ["", None]:
                    if bib_item["citation"] == "" or overwrite:
                        bib_item["citation"] = _get_citation(bib_item["bibkey"])

    with open(json_file, "w") as dst:
        json.dump(nm_meta, dst, indent=4)
