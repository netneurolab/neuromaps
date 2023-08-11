"""Functions for fetching datasets."""

__all__ = [
    'fetch_all_atlases', 'fetch_atlas', 'fetch_civet', 'fetch_fsaverage',
    'fetch_fslr', 'fetch_mni152', 'fetch_regfusion', 'get_atlas_dir',
    'DENSITIES', 'ALIAS', 'available_annotations', 'available_tags',
    'fetch_annotation', "get_annotations_desc", "get_annotations_summary",
    "get_annotations_report"
]

from .atlases import (fetch_all_atlases, fetch_atlas, fetch_civet,  # noqa
                      fetch_fsaverage, fetch_fslr, fetch_mni152,
                      fetch_regfusion, get_atlas_dir, DENSITIES, ALIAS)
from .annotations import (available_annotations, available_tags,  # noqa
<<<<<<< HEAD
                          fetch_annotation)
=======
                          fetch_annotation,  get_annotations_summary, 
                          get_annotations_desc, get_annotations_report)
from .contributions import (upload_annotation)
>>>>>>> [ENH] Continue working on the changes
