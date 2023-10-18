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


def test_run_cookiecutter_and_plugin_tests(cookies, capsys):
    """Create a new plugin via cookiecutter and run its tests."""
    result = cookies.bake(extra_context={"plugin_name": "foo-bar"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "foo-bar"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("src").is_dir()
    assert result.project_path.joinpath("src", "foo_bar", "__init__.py").is_file()
    assert result.project_path.joinpath("src", "foo_bar", "_tests", "test_reader.py").is_file()

    run_tox(str(result.project_path))


def test_run_cookiecutter_and_plugin_tests_with_napari_prefix(cookies, capsys):
    """make sure it's also ok to use napari prefix."""
    result = cookies.bake(extra_context={"plugin_name": "napari-foo"})

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "napari-foo"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("src").is_dir()
    assert result.project_path.joinpath("src", "napari_foo", "__init__.py").is_file()
    assert result.project_path.joinpath("src", "napari_foo", "_tests", "test_reader.py").is_file()


def test_run_cookiecutter_select_plugins(cookies, capsys):
    """make sure it's also ok to use napari prefix."""
    result = cookies.bake(
        extra_context={
            "plugin_name": "anything",
            "include_widget_plugin": "n",
            "include_writer_plugin": "n",
        }
    )

    assert result.exit_code == 0
    assert result.exception is None
    assert result.project_path.name == "anything"
    assert result.project_path.is_dir()
    assert result.project_path.joinpath("src").is_dir()
    assert result.project_path.joinpath("src", "anything", "__init__.py").is_file()
    assert result.project_path.joinpath("src", "anything", "_tests", "test_reader.py").is_file()

    assert not result.project_path.joinpath("src", "anything", "_widget.py").is_file()
    assert not result.project_path.joinpath(
        "src", "anything", "_tests", "test_widget.py"
    ).is_file()
    assert not result.project_path.joinpath("src", "anything", "_writer.py").is_file()
    assert not result.project_path.joinpath(
        "src", "anything", "_tests", "test_writer.py"
    ).is_file()


@pytest.mark.parametrize("include_reader_plugin", [True, False])
@pytest.mark.parametrize("include_writer_plugin", [True, False])
@pytest.mark.parametrize("include_sample_data_plugin", [True, False])
@pytest.mark.parametrize("include_widget_plugin", [True, False])
def test_pre_commit_validity(cookies, include_reader_plugin, include_writer_plugin, include_sample_data_plugin, include_widget_plugin):
    result = cookies.bake(
        extra_context={
            "plugin_name": "anything",
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
        pytest.fail(f"pre-commit failed with output:\n{e.stdout.decode()}\nerrror:\n{e.stderr.decode()}")
