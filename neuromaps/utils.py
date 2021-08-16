# -*- coding: utf-8 -*-
"""
Utility functions
"""

import os
from pathlib import Path
import tempfile
import subprocess


def tmpname(suffix, prefix=None, directory=None):
    """
    Little helper function because :man_shrugging:

    Parameters
    ----------
    suffix : str
        Suffix of created filename

    Returns
    -------
    fn : str
        Temporary filename; user is responsible for deletion
    """

    fd, fn = tempfile.mkstemp(suffix=suffix, prefix=prefix, dir=directory)
    os.close(fd)

    return Path(fn)


def run(cmd, env=None, return_proc=False, quiet=False, **kwargs):
    """
    Runs `cmd` via shell subprocess with provided environment `env`

    Parameters
    ----------
    cmd : str
        Command to be run as single string
    env : dict, optional
        If provided, dictionary of key-value pairs to be added to base
        environment when running `cmd`. Default: None
    return_proc : bool, optional
        Whether to return CompletedProcess object. Default: false
    quiet : bool, optional
        Whether to suppress stdout/stderr from subprocess. Default: False

    Returns
    -------
    proc : subprocess.CompletedProcess
        Process output

    Raises
    ------
    subprocess.CalledProcessError
        If subprocess does not exit cleanly

    Examples
    --------
    >>> from neuromaps import utils
    >>> p = utils.run('echo "hello world"', return_proc=True, quiet=True)
    >>> p.returncode
    0
    >>> p.stdout  # doctest: +SKIP
    'hello world\\n'
    """

    merged_env = os.environ.copy()
    if env is not None:
        if not isinstance(env, dict):
            raise TypeError('Provided `env` must be a dictionary, not {}'
                            .format(type(env)))
        merged_env.update(env)

    opts = dict(check=True, shell=True, universal_newlines=True)
    opts.update(**kwargs)
    if quiet:
        opts.update(dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE))

    try:
        proc = subprocess.run(cmd, env=merged_env, **opts)
    except subprocess.CalledProcessError as err:
        raise subprocess.SubprocessError(
            f'Command failed with non-zero exit status {err.returncode}. '
            f'Error traceback: "{err.stderr.strip()}"'
        )

    if return_proc:
        return proc


def check_fs_subjid(subject_id, subjects_dir=None):
    """
    Checks that `subject_id` exists in provided FreeSurfer `subjects_dir`

    Parameters
    ----------
    subject_id : str
        FreeSurfer subject ID
    subjects_dir : str, optional
        Path to FreeSurfer subject directory. If not set, will inherit from
        the environmental variable $SUBJECTS_DIR. Default: None

    Returns
    -------
    subject_id : str
        FreeSurfer subject ID, as provided
    subjects_dir : str
        Full filepath to `subjects_dir`

    Raises
    ------
    FileNotFoundError
    """

    # check inputs for subjects_dir and subject_id
    if subjects_dir is None or not os.path.isdir(subjects_dir):
        try:
            subjects_dir = os.environ['SUBJECTS_DIR']
        except KeyError:
            subjects_dir = os.getcwd()
    else:
        subjects_dir = os.path.abspath(subjects_dir)

    subjdir = os.path.join(subjects_dir, subject_id)
    if not os.path.isdir(subjdir):
        raise FileNotFoundError('Cannot find specified subject id {} in '
                                'provided subject directory {}.'
                                .format(subject_id, subjects_dir))

    return subject_id, subjects_dir
