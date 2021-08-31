# -*- coding: utf-8 -*-
"""
Functions for fetching annotations (from the internet, if necessary)
"""

from collections import defaultdict
from pathlib import Path
import re
import shutil

from nilearn.datasets.utils import _fetch_file

from neuromaps.datasets.utils import (get_data_dir, get_dataset_info,
                                      _get_token, _get_session)

MATCH = re.compile(
    r'source-(\S+)_desc-(\S+)_space-(\S+)_(?:den|res)-(\d+[k|m]{1,2})_'
)


def _groupby_match(fnames, return_single=False):
    """"
    Groups files in `fnames` by (source, desc, space, res/den)

    Parameters
    ----------
    fnames : list-of-str
        Filenames to be grouped
    return_single : bool, optional
        If there is only group of filenames return a list instead of a dict.
        Default: False

    Returns
    -------
    groups : dict-of-str
        Where keys are tuple (source, desc, space, res/den) and values are
        lists of filenames
    """

    out = defaultdict(list)
    for fn in fnames:
        out[MATCH.search(fn).groups()].append(fn)

    out = {k: v if len(v) > 1 else v[0] for k, v in out.items()}

    if return_single and len(out) == 1:
        out = list(out.values())[0]

    return out


def _match_annot(info, **kwargs):
    """
    Matches datasets in `info` to relevant keys

    Parameters
    ----------
    info : list-of-dict
        Information on annotations
    kwargs : key-value pairs
        Values of data in `info` on which to match

    Returns
    -------
    matched : list-of-dict
        Annotations with specified values for keys
    """

    # tags should always be a list
    tags = kwargs.get('tags')
    if tags is not None and isinstance(tags, str):
        kwargs['tags'] = [tags]

    # 'den' and 'res' are a special case because these are mutually exclusive
    # values (only one will ever be set for a given annotation) so we want to
    # match on _either_, not both, if and only if both are provided as keys.
    # if only one is specified as a key then we should exclude the other!
    denres = []
    for vals in (kwargs.get('den'), kwargs.get('res')):
        vals = [vals] if isinstance(vals, str) else vals
        if vals is not None:
            denres.extend(vals)

    out = []
    for dset in info:
        match = True
        for key in ('source', 'desc', 'space', 'hemi', 'tags', 'format'):
            comp, value = dset.get(key), kwargs.get(key)
            if value is None:
                continue
            elif value is not None and comp is None:
                match = False
            elif isinstance(value, str):
                if value != 'all':
                    match = match and comp == value
            else:
                func = all if key == 'tags' else any
                match = match and func(f in comp for f in value)
        if len(denres) > 0:
            match = match and (dset.get('den') or dset.get('res')) in denres
        if match:
            out.append(dset)

    return out


def available_annotations(source=None, desc=None, space=None, den=None,
                          res=None, hemi=None, tags=None, format=None,
                          return_restricted=False):
    """
    Lists datasets available via :func:`~.fetch_annotation`

    Parameters
    ----------
    source, desc, space, den, res, hemi, tags, format : str or list-of-str
        Values on which to match annotations. If not specified annotations with
        any value for the relevant key will be matched. Default: None
    return_restricted : bool, optional
        Whether to return restricted annotations. These will only be accesible
        with a valid OSF token. Default: True

    Returns
    -------
    datasets : list-of-str
        List of available annotations
    """

    info = _match_annot(get_dataset_info('annotations', return_restricted),
                        source=source, desc=desc, space=space, den=den,
                        res=res, hemi=hemi, tags=tags, format=format)
    fnames = [dset['fname'] for dset in info]

    return list(_groupby_match(fnames, return_single=False).keys())


def available_tags(return_restricted=False):
    """
    Returns available tags for querying annotations

    Parameters
    ----------
    return_restricted : bool, optional
        Whether to return restricted annotations. These will only be accesible
        with a valid OSF token. Default: True


    Returns
    -------
    tags : list-of-str
        Available tags
    """

    tags = set()
    for dset in get_dataset_info('annotations', return_restricted):
        if dset['tags'] is not None:
            tags.update(dset['tags'])
    return sorted(tags)


def fetch_annotation(*, source=None, desc=None, space=None, den=None, res=None,
                     hemi=None, tags=None, format=None, return_single=True,
                     token=None, data_dir=None, verbose=1):
    """
    Downloads files for brain annotations matching requested variables

    Parameters
    ----------
    source, desc, space, den, res, hemi, tags, format : str or list-of-str
        Values on which to match annotations. If not specified annotations with
        any value for the relevant key will be matched. Default: None
    return_single : bool, optional
        If only one annotation is found matching input parameters return the
        list of filepaths instead of the standard dictionary. Default: True
    token : str, optional
        OSF personal access token for accessing restricted annotations. Will
        also check the environmental variable 'NEUROMAPS_OSF_TOKEN' if not
        provided; if that is not set no token will be provided and restricted
        annotations will be inaccessible. Default: None
    data_dir : str, optional
        Path to use as data directory. If not specified, will check for
        environmental variable 'NEUROMAPS_DATA'; if that is not set, will
        use `~/neuromaps-data` instead. Default: None
    verbose : int, optional
        Modifies verbosity of download, where higher numbers mean more updates.
        Default: 1

    Returns
    -------
    data : dict
        Dictionary of downloaded annotations where dictionary keys are tuples
        (source, desc, space, den/res) and values are lists of corresponding
        filenames
    """

    # check input parameters to ensure we're fetching _something_
    supplied = False
    for val in (source, desc, space, den, res, hemi, tags, format):
        if val is not None:
            supplied = True
            break
    if not supplied:
        raise ValueError('Must provide at least one parameters on which to '
                         'match annotations. If you want to fetch all '
                         'annotations set any of the parameters to "all".')

    # get info on datasets we need to fetch
    token = _get_token(token=token)
    return_restricted = False if (token is None or not token) else True
    data_dir = get_data_dir(data_dir=data_dir)
    info = _match_annot(get_dataset_info('annotations', return_restricted),
                        source=source, desc=desc, space=space, den=den,
                        res=res, hemi=hemi, tags=tags, format=format)
    if verbose > 1:
        print(f'Identified {len(info)} datsets matching specified parameters')

    # get session for requests
    session = _get_session(token=token)

    # TODO: current work-around to handle that _fetch_files() does not support
    # session instances. hopefully a future version will and we can just use
    # that function to handle this instead of calling _fetch_file() directly
    data = []
    for dset in info:
        fn = Path(data_dir) / 'annotations' / dset['rel_path'] / dset['fname']
        if not fn.exists():
            dl_file = _fetch_file(dset['url'], str(fn.parent), verbose=verbose,
                                  md5sum=dset['checksum'], session=session)
            shutil.move(dl_file, fn)
        data.append(str(fn))

    return _groupby_match(data, return_single=return_single)
