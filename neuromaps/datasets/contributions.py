# -*- coding: utf-8 -*-
"""
Workflow for adding new datasets to `neuromaps`
"""

from base64 import b64encode
import hashlib
import os
from pathlib import Path
import warnings

import nibabel as nib
import requests

from neuromaps.datasets import _osf
from neuromaps.datasets.annotations import MATCH, available_annotations
from neuromaps.datasets.atlases import DENSITIES
from neuromaps.datasets.utils import _get_token

HEROKU = 'https://neuromaps-web.herokuapp.com'
VERT_MAP = {
    163842: '164k',
    40962: '41k',
    32492: '32k',
    10242: '10k',
    7842: '8k',
    4002: '4k',
    2562: '3k'
}
REV_VERT_MAP = {v: k for k, v in VERT_MAP.items()}


def upload_annotation(files, user, osf_token=None, nmweb_token=None):
    """
    Workflow for contributing new brain annotation `files` to `neuromaps`

    Parameters
    ----------
    files : str or os.PathLike or tuple
        File(s) to be contributed
    user : str
        E-mail address that can be used to contact you in case the `neuromaps`
        maintainers have questions about the uploaded files. Default: None
    osf_token : str, optional
        Personal access token with authorization to OSF repository. Only needed
        if trying to upload files large than 30 MB. Default: None
    nmweb_token : str, optional
        Personal access token for `neuromaps-web` server. If provided (and
        authorized) a PR will be created automatically. Default: None

    Returns
    -------
    response : requests.Response
        Response object from `neuromaps-web` API
    """

    url = HEROKU
    if int(os.environ.get('NMWEB_DEBUG', 0)):
        url = 'http://127.0.0.1:5000'
    osf_token = _get_token(osf_token)
    if nmweb_token is None:
        nmweb_token = os.environ.get('NEUROMAPS_NMWEB_TOKEN', None)

    if isinstance(files, (str, os.PathLike)):
        files = (files,)

    tags = []
    if tags is not None:
        if isinstance(tags, str):
            tags = [tags]
        tags = list(tags)

    package = []
    package_hash = hashlib.md5()
    for fname in files:
        # filesize check (limit to <30 MB)
        fsize = os.stat(fname).st_size / (1024 ** 2)
        if fsize > 30:
            auth = False
            if osf_token is not None:
                resp = requests.post(
                    f'{url}/authenticate', headers={'osf-token': {osf_token}}
                )
                if resp.status_code == 200:
                    auth = True
                else:
                    warnings.warn('Token authorization failed; admin access '
                                  'to OSF repo not permitted.')
            if not auth:
                raise ValueError(f'Provided file {fname} is too large. Max '
                                 'file size for brain map is 30 MB. '
                                 f'Received: {fsize}')

        # basic filename checks for expected keys
        base = os.path.basename(fname)
        info = _osf.parse_filename(base, return_ext=False)
        for key in ['source', 'desc', 'space']:
            if key not in info:
                raise ValueError(f'Filename must have {key} key: {base}')
        if 'den' in info and 'hemi' not in info:
            raise ValueError('If provided file has "den" key it must also '
                             f'have "hemi" key: {base}')

        # check that space + den/res match
        surf_space = {'fsLR', 'fsaverage', 'civet'}
        if 'res' in info:
            if info['space'] != 'MNI152':
                raise ValueError('Only valid "space" for file with "res" key '
                                 f'is "MNI152". Received: {base}')
            if info['res'] not in DENSITIES.get('MNI152'):
                raise ValueError('Provided value for "res" is not valid. Must '
                                 f'be one of {DENSITIES.get("MNI152")}. '
                                 f'Received: {base}')
            if ''.join(Path(base).suffixes) != '.nii.gz':
                raise ValueError('Provided volumetric image must have .nii.gz '
                                 f'suffix. Received: {base}')
            img = nib.load(fname)
            img = nib.funcs.squeeze_image(img)
            vox = nib.affines.voxel_sizes(img.affine)
            if len(img.shape) > 3:
                raise ValueError('Provided NIFTI image has multiple volumes.'
                                 'Must provide a 3D image. Invalid file: '
                                 f'{base}')
            if not all(int(info['res'][:-2]) == v for v in vox):
                raise ValueError('Provided NIFTI image has different voxel '
                                 'resolution than specified in filename. '
                                 f'Expected: {info["res"]}. Received: '
                                 f'{vox}')
        elif 'den' in info:
            if info['space'] not in surf_space:
                raise ValueError('Only valid "space" for file with "den" key'
                                 f'are {surf_space}. Received: {base}')
            if info['den'] not in DENSITIES.get(info['space']):
                raise ValueError('Provided value for "den" is not valid. Must '
                                 f'be one of {DENSITIES.get(info["space"])}. '
                                 f'Received: {base}')
            if ''.join(Path(base).suffixes) != '.func.gii':
                raise ValueError('Provided surface image must have .func.gii '
                                 f'suffix. Received: {base}')
            img = nib.load(fname)
            shape = img.agg_data().shape
            if len(shape) > 1:
                raise ValueError('Provided GIFTI image has more than one data '
                                 'array. Only single array files are '
                                 f'supported. Invalid file: {base}')
            if VERT_MAP[shape[0]] != info['den']:
                raise ValueError('Provided GIFTI image has different density '
                                 'than specified in filename. Expected: '
                                 f'{info["den"]}. Received: '
                                 f'{REV_VERT_MAP[shape[0]]}')
        else:
            raise ValueError('Filename must have one of "den" (surface) or '
                             f'"res" (volumetric) keys: {base}')

        # check correct ordering of keys in filename
        if MATCH.search(base) is None:
            raise ValueError('Provided filename keys must be in order: '
                             '(1) "source", (2) "desc", (3) "space", (4) "den"'
                             f'/"res", (5) "hemi". Received: {base}')

        # check that file info does not match an existing annotation!
        if len(available_annotations(info)) != 0:
            raise ValueError('Provided file already matches existing '
                             'annotation.')

        # fill additional information on file
        bytestream = img.to_bytes()
        package_hash.update(bytestream)
        info = _osf.complete_json([info])[0]
        info = _osf.clean_minimal_keys(_osf.generate_auto_keys(info))
        info['checksum'] = hashlib.md5(bytestream).hexdigest()
        info['tags'] = tags
        info['data'] = b64encode(nib.load(fname).to_bytes()).decode()
        package.append(info)

    # upload package
    resp = requests.post(f'{url}/upload-files',
                         json={'data': package,
                               'md5': package_hash.hexdigest()},
                         headers={'user-email': user,
                                  'osf-token': osf_token,
                                  'nmweb-token': nmweb_token})
    if resp.status_code != 200:
        resp.reason = resp.text
        resp.raise_for_status()
        raise requests.HTTPError(f'{resp.status_code}: {resp.text}')

    return resp
