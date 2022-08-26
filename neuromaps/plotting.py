# -*- coding: utf-8 -*-
"""
Functionality for plotting
"""

from matplotlib import colors as mcolors, pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa
from nilearn.plotting import plot_surf
import numpy as np

from neuromaps.datasets import ALIAS, fetch_atlas
from neuromaps.images import load_gifti
from neuromaps.transforms import _check_hemi

HEMI = dict(L='left', R='right')
plt.cm.register_cmap(
    'caret_blueorange', mcolors.LinearSegmentedColormap.from_list('blend', [
        '#00d2ff', '#009eff', '#006cfe', '#0043fe',
        '#fd4604', '#fe6b01', '#ffd100', '#ffff04'
    ])
)


def plot_surf_template(data, template, density, surf='inflated',
                       hemi=None, data_dir=None, mask_medial=True, **kwargs):
    """
    Plots `data` on `template` surface

    Parameters
    ----------
    data : str or os.PathLike or tuple-of-str
        Path to data file(s) to be plotted. If tuple, assumes (left, right)
        hemisphere.
    template : {'civet', 'fsaverage', 'fsLR'}
        Template on which `data` is defined
    density : str
        Resolution of template
    surf : str, optional
        Surface on which `data` should be plotted. Must be valid for specified
        `space`. Default: 'inflated'
    hemi : {'L', 'R'}, optional
        If `data` is not a tuple, which hemisphere it should be plotted on.
        Default: None
    mask_medial : bool, optional
        Whether to mask vertices along the medial wall. Default: True
    kwargs : key-value pairs
        Passed directly to `nilearn.plotting.plot_surf`

    Returns
    -------
    fig : matplotlib.Figure instance
        Plotted figure
    """

    atlas = fetch_atlas(template, density, data_dir=data_dir, verbose=0)
    template = ALIAS.get(template, template)
    if template == 'MNI152':
        raise ValueError('Cannot plot MNI152 on the surface. Try performing '
                         'registration fusion to project data to the surface '
                         'and plotting the projection instead.')
    surf, medial = atlas[surf], atlas['medial']

    opts = dict(alpha=1.0, threshold=np.spacing(1))
    opts.update(**kwargs)
    if kwargs.get('bg_map') is not None and kwargs.get('alpha') is None:
        opts['alpha'] = 'auto'

    data, hemispheres = zip(*_check_hemi(data, hemi))
    n_surf = len(data)
    fig, axes = plt.subplots(n_surf, 2, subplot_kw={'projection': '3d'})
    axes = (axes,) if n_surf == 1 else axes.T
    for row, hemi, img in zip(axes, hemispheres, data):
        geom = load_gifti(getattr(surf, hemi)).agg_data()
        img = load_gifti(img).agg_data().astype('float32')
        # set medial wall to NaN; this will avoid it being plotted
        if mask_medial:
            med = load_gifti(getattr(medial, hemi)).agg_data().astype(bool)
            img[np.logical_not(med)] = np.nan

        for ax, view in zip(row, ['lateral', 'medial']):
            ax.disable_mouse_rotation()
            plot_surf(geom, img, hemi=HEMI[hemi], axes=ax, view=view, **opts)
            poly = ax.collections[0]
            poly.set_facecolors(
                _fix_facecolors(ax, poly._original_facecolor,
                                *geom, view, hemi)
            )

    if not opts.get('colorbar', False):
        fig.tight_layout()
        if n_surf == 1:
            fig.subplots_adjust(wspace=-0.1)
        else:
            fig.subplots_adjust(wspace=-0.4, hspace=-0.15)

    return fig


def _fix_facecolors(ax, facecolors, vertices, faces, view, hemi):
    """
    Updates `facecolors` to reflect shading of mesh geometry

    Parameters
    ----------
    ax : plt.Axes3dSubplot
        Axis instance
    facecolors : (F,) array_like
        Original facecolors of plot
    vertices : (V, 3)
        Vertices of surface mesh
    faces : (F, 3)
        Triangles of surface mesh
    view : {'lateral', 'medial'}
        Plotted view of brain

    Returns
    -------
    colors : (F,) array_like
        Updated facecolors with approriate shading
    """

    hemi_view = {'R': {'lateral': 'medial', 'medial': 'lateral'}}
    views = {
        'lateral': plt.cm.colors.LightSource(azdeg=225, altdeg=19.4712),
        'medial': plt.cm.colors.LightSource(azdeg=45, altdeg=19.4712)
    }

    # reverse medial / lateral views if plotting right hemisphere
    view = hemi_view.get(hemi, {}).get(view, view)
    # re-shade colors
    normals = ax._generate_normals(vertices[faces])
    colors = ax._shade_colors(np.asarray(facecolors), normals, views[view])

    return colors
