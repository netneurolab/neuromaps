# -*- coding: utf-8 -*-
"""For testing neuromaps.transforms functionality."""

import pytest

from neuromaps import transforms


@pytest.mark.xfail
def test__regfusion_project():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test__vol_to_surf():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test_mni152_to_civet():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test_mni152_to_fsaverage():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test_mni152_to_fslr():
    """Test projecting a volume to a surface."""
    assert False


@pytest.mark.xfail
def test_mni152_to_mni152():
    """Test projecting a volume to a surface."""
    assert False


def test__check_hemi():
    """Test checking the hemisphere."""
    d, h = zip(*transforms._check_hemi('test', 'L'))
    assert d == ('test',) and h == ('L',)

    for d, h in (('test', None), ('test', 'invalid_hemi')):
        with pytest.raises(ValueError):
            transforms._check_hemi(d, h)


@pytest.mark.xfail
def test__surf_to_surf():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_civet_to_fslr():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fslr_to_civet():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_civet_to_fsaverage():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fsaverage_to_civet():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fslr_to_fsaverage():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fsaverage_to_fslr():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_civet_to_civet():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fslr_to_fslr():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.xfail
def test_fsaverage_to_fsaverage():
    """Test projecting a surface to another surface."""
    assert False


@pytest.mark.parametrize('method, operation', [
    ('linear', '-metric-resample'),
    ('nearest', '-label-resample'),
])
def test_surface_resampling_literal_paths(tmp_path, method, operation):
    """Keep surface paths literal when invoking Workbench."""
    import subprocess
    from unittest.mock import patch

    image = (tmp_path / 'input scan;literal.func.gii').resolve()
    atlas = tmp_path / 'atlas files;literal'
    output = tmp_path / 'output scan;literal.func.gii'
    output.touch()
    sentinel = object()
    with patch.multiple(
        transforms,
        fetch_atlas=lambda *args: None,
        get_atlas_dir=lambda *args: atlas,
        tmpname=lambda *args: output,
        load_data=lambda *args: sentinel,
        construct_shape_gii=lambda data: data,
    ), patch('subprocess.run', return_value=subprocess.CompletedProcess([], 0)) as run:
        result = transforms._surf_to_surf(
            image,
            {'space': 'fsaverage', 'den': '3k', 'trg': ''},
            {'space': 'fsLR', 'den': '32k', 'trg': ''},
            method=method, hemi='L',
        )

    assert result == (sentinel,)
    assert run.call_count == 2
    resample, mask = run.call_args_list
    assert resample.args[0][:3] == ['wb_command', operation, str(image)]
    assert resample.args[0][3:5] == [
        str(atlas / 'tpl-fsaverage_den-3k_hemi-L_sphere.surf.gii'),
        str(atlas / 'tpl-fsLR_den-32k_hemi-L_sphere.surf.gii'),
    ]
    assert resample.args[0][6] == str(output)
    assert resample.args[0][8:10] == [
        str(atlas / 'tpl-fsaverage_den-3k_hemi-L_desc-vaavg_midthickness.shape.gii'),
        str(atlas / 'tpl-fsLR_den-32k_hemi-L_desc-vaavg_midthickness.shape.gii'),
    ]
    assert resample.args[0][11] == str(
        atlas / 'tpl-fsaverage_den-3k_hemi-L_desc-nomedialwall_dparc.label.gii'
    )
    assert mask.args[0] == [
        'wb_command', '-metric-mask', str(output),
        str(atlas / 'tpl-fsLR_den-32k_hemi-L_desc-nomedialwall_dparc.label.gii'),
        str(output),
    ]
    assert all(call.kwargs['shell'] is False for call in run.call_args_list)
