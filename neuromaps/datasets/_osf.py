# -*- coding: utf-8 -*-
"""Functions for working with data/osf.json file."""

import os
from pprint import pprint
from pkg_resources import resource_filename

try:
    # nilearn 0.10.3
    from nilearn.datasets._utils import _md5_sum_file
except ImportError:
    from nilearn.datasets.utils import _md5_sum_file

from neuromaps.datasets.utils import \
    FNAME_SURF_KEYS, FNAME_VOL_KEYS, INFO_REFS_KEYS, INFO_DEMO_KEYS, COND_KEYS
from neuromaps.datasets.utils import _get_session, generate_auto_keys

# distribution JSON
OSFJSON = resource_filename(
    'neuromaps', os.path.join('datasets', 'data', 'osf.json')
)


def _generate_template(data_format, data_tuple, file_path=None):
    """

    Helper function for generating a template for a new annotation

    This function generates item sample for the `data/osf.json` and the
    `data/info.json` files. You can then rename & upload the file to osf
    storage and fill the rest of the dictionary, before adding it to the
    corresponding files.

    Parameters
    ----------
    data_format : str, {'surface', 'volume'}
        Format of the annotation
    data_tuple : tuple-of-str
        If `data_format = 'surface'` input should be
        ('source', 'desc', 'space', 'den', 'hemi')
        If `data_format = 'volume'`, input should be
        ('source', 'desc', 'space', 'res')
    file_path : str, optional
        Full path to file to generate checksum for.
        Does not need to be renamed. Default: None
    """

    osf_dict = {}
    info_dict = {'annot': {}}

    if data_format == 'surface':
        for i, key in enumerate(FNAME_SURF_KEYS):
            osf_dict[key] = data_tuple[i]
            if key != 'hemi':
                info_dict['annot'][key] = data_tuple[i]
    elif data_format == 'volume':
        for i, key in enumerate(FNAME_VOL_KEYS):
            osf_dict[key] = data_tuple[i]
            info_dict["annot"][key] = data_tuple[i]
    else:
        raise ValueError('Wrong `data_format`!')

    osf_dict = generate_auto_keys(osf_dict, file_path)

    osf_dict.update({key: None for key in COND_KEYS})

    info_dict['refs'] = {key: None for key in INFO_REFS_KEYS}
    info_dict['demographics'] = {key: None for key in INFO_DEMO_KEYS}

    pprint(osf_dict, sort_dicts=False)

    pprint(info_dict, sort_dicts=False)


def _get_url(fname, project, token=None):
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
