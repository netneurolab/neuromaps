__all__ = ['resample_images', 'correlate_images']

from brainnotation.resampling import resample_images
from brainnotation.stats import correlate_images

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions
