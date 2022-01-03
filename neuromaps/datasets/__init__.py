"""
Functions for fetching datasets
"""

__all__ = [
    'fetch_all_atlases', 'fetch_atlas', 'fetch_civet', 'fetch_fsaverage',
    'fetch_fslr', 'fetch_mni152', 'fetch_regfusion', 'get_atlas_dir',
    'DENSITIES', 'ALIAS', 'available_annotations', 'available_tags',
    'fetch_annotation'
]

# TODO: remove after nilearn v0.9 release
import warnings
warnings.filterwarnings('ignore', message='Fetchers from the nilearn.datasets',
                        category=FutureWarning)

from .atlases import (fetch_all_atlases, fetch_atlas, fetch_civet,  # noqa
                      fetch_fsaverage, fetch_fslr, fetch_mni152,
                      fetch_regfusion, get_atlas_dir, DENSITIES, ALIAS)
from .annotations import (available_annotations, available_tags,  # noqa
                          fetch_annotation)
from .contributions import (upload_annotation)