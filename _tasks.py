from argparse import ArgumentParser
import logging
import os
from pathlib import Path
import re
import subprocess
import sys


def module_name_pep8_compliance(module_name):
    """Validate that the plugin module name is PEP8 compliant."""
    if not re.match(r"^[a-z][_a-z0-9]+$", module_name):
        link = "https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
        logger.error("Module name should be pep-8 compliant.")
        logger.error(f"  More info: {link}")
        sys.exit(1)


def pypi_package_name_compliance(plugin_name):
    """Check there are no underscores in the plugin name"""
    if re.search(r"_", plugin_name):
        logger.error("PyPI.org and pip discourage package names with underscores.")
        sys.exit(1)


def validate_manifest(module_name, project_directory):
    """Validate the new plugin repository against napari requirements."""
    try:
        from npe2 import PluginManifest
    except ImportError as e:
        logger.error("npe2 is not installed. Skipping manifest validation.")
        return True

    current_directory = Path('.').absolute()
    if (current_directory.match(project_directory) and not Path(project_directory).is_absolute()):
        project_directory = current_directory

    path=Path(project_directory) / "src" / Path(module_name) / "napari.yaml"

    valid = False
    try:
        pm = PluginManifest.from_file(path)
        msg = f"✔ Manifest for {(pm.display_name or pm.name)!r} valid!"
        valid = True
    except PluginManifest.ValidationError as err:
        msg = f"🅇 Invalid! {err}"
        logger.error(msg.encode("utf-8"))
        sys.exit(1)
    except Exception as err:
        msg = f"🅇 Failed to read {path!r}. {type(err).__name__}: {err}"
        logger.error(msg.encode("utf-8"))
        sys.exit(1)
    else:
        logger.info(msg.encode("utf-8"))
        return valid


def initialize_new_repository(
        install_precommit=False,
        plugin_name="napari-foobar",
        github_repository_url="provide later",
        github_username_or_organization="githubuser",
    ):
    """Initialize new plugin repository with git, and optionally pre-commit."""

    msg = ""
    # try to run git init
    try:
        subprocess.run(["git", "init", "-q"])
        subprocess.run(["git", "checkout", "-b", "main"])
    except Exception:
        logger.error("Error in git initialization.")

    if install_precommit is True:
        # try to install and update pre-commit
        try:
            print("install pre-commit ...")
            subprocess.run(["python", "-m", "pip", "install", "pre-commit"], stdout=subprocess.DEVNULL)
            print("updating pre-commit...")
            subprocess.run(["pre-commit", "autoupdate"], stdout=subprocess.DEVNULL)
            subprocess.run(["git", "add", "."])
            subprocess.run(["pre-commit", "run", "black", "-a"], capture_output=True)
        except Exception:
            logger.error("Error pip installing then running pre-commit.")

    try:
        subprocess.run(["git", "add", "."])
        subprocess.run(["git", "commit", "-q", "-m", "initial commit"])
    except Exception:
        logger.error("Error creating initial git commit.")
        msg += f"""
Your plugin template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
(this is also important for version control!)

    cd {plugin_name}
    git init -b main
    git add .
    git commit -m 'initial commit'

    # you probably want to install your new package into your environment
    pip install -e .
"""
    else:
        msg +=f"""
Your plugin template is ready!  Next steps:

1. `cd` into your new directory

    cd {plugin_name}
    # you probably want to install your new package into your env
    pip install -e .
"""

    if install_precommit is True:
        # try to install and update pre-commit
        # installing after commit to avoid problem with comments in setup.cfg.
        try:
            print("install pre-commit hook...")
            subprocess.run(["pre-commit", "install"])
        except Exception:
            logger.error("Error at pre-commit install, skipping pre-commit")

    if github_repository_url != 'provide later':
        msg += f"""
    2. Create a github repository with the name '{plugin_name}':
    https://github.com/{github_username_or_organization}/{plugin_name}.git

    3. Add your newly created github repo as a remote and push:

        git remote add origin https://github.com/{github_username_or_organization}/{plugin_name}.git
        git push -u origin main

    4. The following default URLs have been added to `setup.cfg`:

        Bug Tracker = https://github.com/{github_username_or_organization}/{plugin_name}/issues
        Documentation = https://github.com/{github_username_or_organization}/{plugin_name}#README.md
        Source Code = https://github.com/{github_username_or_organization}/{plugin_name}
        User Support = https://github.com/{github_username_or_organization}/{plugin_name}/issues

        These URLs will be displayed on your plugin's napari hub page.
        You may wish to change these before publishing your plugin!"""
    else:
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

    msg += """
    5. Read the README for more info: https://github.com/napari/cookiecutter-napari-plugin

    6. We've provided a template description for your plugin page at `.napari/DESCRIPTION.md`.
    You'll likely want to edit this before you publish your plugin.

    7. Consider customizing the rest of your plugin metadata for display on the napari hub:
    https://github.com/chanzuckerberg/napari-hub/blob/main/docs/customizing-plugin-listing.md
    """
    return msg


if __name__=="__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger = logging.getLogger("pre_gen_project")
    parser = ArgumentParser()
    parser.add_argument("--plugin_name",
                        dest="plugin_name",
                        help="The name of your plugin")
    parser.add_argument("--module_name",
                        dest="module_name",
                        help="Plugin module name")
    parser.add_argument("--project_directory",
                        dest="project_directory",
                        help="Project directory")
    parser.add_argument("--install_precommit",
                        dest="install_precommit",
                        help="Install pre-commit",
                        default=False)
    parser.add_argument("--github_repository_url",
                        dest="github_repository_url",
                        help="Github repository URL",
                        default='provide later')
    parser.add_argument("--github_username_or_organization",
                        dest="github_username_or_organization",
                        help="Github user or organisation name",
                        default='githubuser')
    args = parser.parse_args()

    module_name_pep8_compliance(args.module_name)
    pypi_package_name_compliance(args.plugin_name)
    validate_manifest(args.module_name, args.project_directory)
    msg = initialize_new_repository(
        install_precommit=bool(args.install_precommit),
        plugin_name=args.plugin_name,
        github_repository_url=args.github_repository_url,
        github_username_or_organization=args.github_username_or_organization,
    )
    print(msg)
