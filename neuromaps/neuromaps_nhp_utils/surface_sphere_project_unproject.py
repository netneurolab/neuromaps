
import os
from niwrap import workbench as wb


def surface_sphere_project_unproject(sphere_in, sphere_project_to, sphere_unproject_from, sphere_out):
    """Project and unproject a surface from one sphere to another.

    Parameters
    ----------
    sphere_in : str
        Path to input spherical surface.
    sphere_project_to : str
        Path to spherical surface to project to.
    sphere_unproject_from : str
        Path to spherical surface to unproject from.
    sphere_out : str
        Path to output spherical surface.
    """
    wb.surface_sphere_project_unproject(sphere_in, sphere_project_to, sphere_unproject_from, sphere_out)
    return sphere_out
    