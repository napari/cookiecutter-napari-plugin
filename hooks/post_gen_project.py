#!/usr/bin/env python

import logging
import os
import shutil
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("post_gen_project")

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
ALL_TEMP_FOLDERS = ["licenses"]



def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.debug("Remove temporary folder: %s", folder)
        shutil.rmtree(folder, ignore_errors=True)


def remove_unrequested_plugin_examples():
    module = "{{ cookiecutter.module_name }}"
    {% for key, value in cookiecutter.items() %}
    {% if key.startswith('include_') and key.endswith("_plugin") and value != 'y' %}
    name = "{{ key }}".replace("include_", "").replace("_plugin", "")
    remove_file(f"src/{module}/_{name}.py")
    remove_file(f"src/{module}/_tests/test_{name}.py")
    logger.debug(f"removing {module}/_{name}.py")
    {% endif %}
    {% endfor %}


def validate_manifest():
    try:
        from npe2 import PluginManifest
    except ImportError as e:
        print("npe2 is not installed. Skipping manifest validation.")
        return True

    path=Path(PROJECT_DIRECTORY) / "src" / "{{cookiecutter.module_name}}" / "napari.yaml"

    valid = False
    try:
        pm = PluginManifest.from_file(path)
        msg = f"✔ Manifest for {(pm.display_name or pm.name)!r} valid!"
        valid = True
    except PluginManifest.ValidationError as err:
        msg = f"🅇 Invalid! {err}"
    except Exception as err:
        msg = f"🅇 Failed to read {path!r}. {type(err).__name__}: {err}"

    print(msg.encode("utf-8"))
    return valid


if __name__ == "__main__":
    remove_temp_folders(ALL_TEMP_FOLDERS)
    remove_unrequested_plugin_examples()
    valid=validate_manifest()

    msg = ''
    # try to run git init
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "checkout", "-b", "main"])
    except Exception:
        pass
{% if cookiecutter.install_precommit == 'y' %}
    # try to install and update pre-commit
    try:
        print("install pre-commit ...")
        subprocess.run(["pip", "install", "pre-commit"], stdout=subprocess.DEVNULL)
        print("updating pre-commit...")
        subprocess.run(["pre-commit", "autoupdate"], stdout=subprocess.DEVNULL)
        subprocess.run(["git", "add", "."])
        subprocess.run(["pre-commit", "run", "black", "-a"], capture_output=True)
    except Exception:
        pass
{% endif %}
    try:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
    except Exception:
        msg += """
Your plugin template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
   (this is also important for version control!)

     cd {{ cookiecutter.plugin_name }}
     git init -b main
     git add .
     git commit -m 'initial commit'

     # you probably want to install your new package into your environment
     pip install -e ."""
    else:
        msg +="""
Your plugin template is ready!  Next steps:

1. `cd` into your new directory

     cd {{ cookiecutter.plugin_name }}
     # you probably want to install your new package into your env
     pip install -e ."""

{% if cookiecutter.install_precommit == 'y' %}
    # try to install and update pre-commit
    # installing after commit to avoid problem with comments in setup.cfg.
    try:
        print("install pre-commit hook...")
        subprocess.run(["pre-commit", "install"])
    except Exception:
        pass
{% endif %}

{% if cookiecutter.github_repository_url != 'provide later' %}
    msg += """
2. Create a github repository with the name '{{ cookiecutter.plugin_name }}':
   https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.plugin_name }}.git

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/{{ cookiecutter.github_username_or_organization }}/{{ cookiecutter.plugin_name }}.git
     git push -u origin main

4. The following default URLs have been added to `setup.cfg`:

    Bug Tracker = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/issues
    Documentation = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}#README.md
    Source Code = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}
    User Support = https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/issues

    These URLs will be displayed on your plugin's napari hub page.
    You may wish to change these before publishing your plugin!"""

{% else %}
    msg += """
2. Create a github repository for your plugin:
   https://github.com/new

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/your-repo-username/your-repo-name.git
     git push -u origin main

   Don't forget to add this url to setup.cfg!

     [metadata]
     url = https://github.com/your-repo-username/your-repo-name.git

4. Consider adding additional links for documentation and user support to setup.cfg
   using the project_urls key e.g.

    [metadata]
    project_urls =
        Bug Tracker = https://github.com/your-repo-username/your-repo-name/issues
        Documentation = https://github.com/your-repo-username/your-repo-name#README.md
        Source Code = https://github.com/your-repo-username/your-repo-name
        User Support = https://github.com/your-repo-username/your-repo-name/issues"""
{% endif %}
    msg += """
5. Read the README for more info: https://github.com/napari/cookiecutter-napari-plugin

6. We've provided a template description for your plugin page at `.napari/DESCRIPTION.md`.
   You'll likely want to edit this before you publish your plugin.

7. Consider customizing the rest of your plugin metadata for display on the napari hub:
   https://github.com/chanzuckerberg/napari-hub/blob/main/docs/customizing-plugin-listing.md
"""

    print(msg)
