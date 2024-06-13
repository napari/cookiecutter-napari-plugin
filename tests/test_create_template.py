"""
test_create_template
--------------------
"""


import os
import subprocess

import pytest


def run_tox(plugin):
    """Run the tox suite of the newly created plugin."""
    try:
        subprocess.check_call(
            ["tox", "-c", os.path.join(plugin, "tox.ini"), "-e", "py", "--", plugin]
        )
    except subprocess.CalledProcessError as e:
        pytest.fail("Subprocess fail", pytrace=True)


@pytest.mark.parametrize("include_reader_plugin", [True, False])
@pytest.mark.parametrize("include_writer_plugin", [True, False])
@pytest.mark.parametrize("include_sample_data_plugin", [True, False])
@pytest.mark.parametrize("include_widget_plugin", [True, False])
def test_run_plugin_tests(copie, capsys, include_reader_plugin, include_writer_plugin, include_sample_data_plugin, include_widget_plugin):
    """Create a new plugin with the napari plugin template and run its tests."""
    result = copie.copy(extra_answers={
        "plugin_name": "foo-bar",
        "display_name": "Foo Bar",
        "short_description": "Super fast foo for all the bars",
        "full_name": "napari bot",
        "email": "etal@example.com",
        "github_username_or_organization": "napari",
        "include_reader_plugin": include_reader_plugin,
        "include_writer_plugin": include_writer_plugin,
        "include_sample_data_plugin": include_sample_data_plugin,
        "include_widget_plugin": include_widget_plugin,
        })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir/"README.md") as f:
        assert f.readline() == "# foo-bar\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", "foo_bar", "__init__.py").is_file()

    test_path = result.project_dir.joinpath("src", "foo_bar", "_tests")
    if include_reader_plugin is True:
        assert (test_path / "test_reader.py").is_file()
    if include_writer_plugin is True:
        assert (test_path / "test_writer.py").is_file()
    if include_sample_data_plugin is True:
        assert (test_path / "test_sample_data.py").is_file()
    if include_widget_plugin is True:
        assert (test_path / "test_widget.py").is_file()

    # if all are False there are no modules or tests
    if True in {include_reader_plugin, include_writer_plugin, include_sample_data_plugin, include_widget_plugin}:
        run_tox(str(result.project_dir))


def test_run_plugin_tests_with_napari_prefix(copie, capsys):
    """make sure it's also ok to use napari prefix."""
    name = "napari-foo"
    result = copie.copy(extra_answers={
        "plugin_name": name,
        "display_name": "napari Foo",
        "short_description": "Super fast foo for all the bars",
        "full_name": "napari bot",
        "email": "etal@example.com",
        "github_username_or_organization": "napari",
        })

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir/"README.md") as f:
        assert f.readline() == f"# {name}\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", "napari_foo", "__init__.py").is_file()
    assert result.project_dir.joinpath("src", "napari_foo", "_tests", "test_reader.py").is_file()


def test_run_select_plugins(copie, capsys):
    """make sure it's also ok to use napari prefix."""
    name = "anything"
    result = copie.copy(
        extra_answers={
            "plugin_name": name,
            "display_name": "Foo Bar",
            "short_description": "Super fast foo for all the bars",
            "full_name": "napari bot",
            "email": "etal@example.com",
            "github_username_or_organization": "napari",
            "include_widget_plugin": "n",
            "include_writer_plugin": "n",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_dir.is_dir()
    with open(result.project_dir/"README.md") as f:
        assert f.readline() == f"# {name}\n"
    assert result.project_dir.joinpath("src").is_dir()
    assert result.project_dir.joinpath("src", name, "__init__.py").is_file()
    assert result.project_dir.joinpath("src", name, "_tests", "test_reader.py").is_file()

    assert not result.project_dir.joinpath("src", "anything", "_widget.py").is_file()
    assert not result.project_dir.joinpath(
        "src", "anything", "_tests", "test_widget.py"
    ).is_file()
    assert not result.project_dir.joinpath("src", "anything", "_writer.py").is_file()
    assert not result.project_dir.joinpath(
        "src", "anything", "_tests", "test_writer.py"
    ).is_file()


@pytest.mark.parametrize("include_reader_plugin", [True, False])
@pytest.mark.parametrize("include_writer_plugin", [True, False])
@pytest.mark.parametrize("include_sample_data_plugin", [True, False])
@pytest.mark.parametrize("include_widget_plugin", [True, False])
def test_pre_commit_validity(copie, include_reader_plugin, include_writer_plugin, include_sample_data_plugin, include_widget_plugin):
    result = copie.copy(
        extra_answers={
            "plugin_name": "anything",
            "display_name": "Foo Bar",
            "short_description": "Super fast foo for all the bars",
            "full_name": "napari bot",
            "email": "etal@example.com",
            "github_username_or_organization": "napari",
            "include_reader_plugin": include_reader_plugin,
            "include_writer_plugin": include_writer_plugin,
            "include_sample_data_plugin": include_sample_data_plugin,
            "include_widget_plugin": include_widget_plugin,
            "install_precommit": True,
        }
    )
    result.project_path.joinpath("setup.cfg").is_file()
    try:
        subprocess.run(["pre-commit", "run", "--all", "--show-diff-on-failure"], cwd=str(result.project_path), check=True, capture_output=True)
    except subprocess.CalledProcessError as e:
        pytest.fail(f"pre-commit failed with output:\n{e.stdout.decode()}\nerror:\n{e.stderr.decode()}")
