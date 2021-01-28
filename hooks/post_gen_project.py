#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import shutil

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("post_gen_project")

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)
DOCS_SOURCES = "docs_sources"
ALL_TEMP_FOLDERS = [DOCS_SOURCES, "licenses"]
DOCS_FILES_BY_TOOL = {
    "mkdocs": ["index.md", "/mkdocs.yml"],
    "sphinx": ["conf.py", "index.rst", "make.bat", "Makefile"],
}


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


def move_docs_files(docs_tool, docs_files, docs_sources):
    if docs_tool == "none":
        return

    root = os.getcwd()
    docs = "docs"

    logger.debug("Initializing docs for %s", docs_tool)
    if not os.path.exists(docs):
        os.mkdir(docs)

    for item in docs_files[docs_tool]:
        dst, name = (root, item[1:]) if item.startswith("/") else (docs, item)
        src_path = os.path.join(docs_sources, docs_tool, name)
        dst_path = os.path.join(dst, name)

        logger.debug("Moving %s to %s.", src_path, dst_path)
        if os.path.exists(dst_path):
            os.unlink(dst_path)

        os.rename(src_path, dst_path)


def remove_temp_folders(temp_folders):
    for folder in temp_folders:
        logger.debug("Remove temporary folder: %s", folder)
        shutil.rmtree(folder, ignore_errors=True)


def remove_unrequested_plugin_examples():
    module = "{{ cookiecutter.module_name }}"
    {% for key, value in cookiecutter.items() %}
    {% if key.startswith('include_') and key.endswith("_plugin") and value != 'y' %}
    name = "{{ key }}".replace("include_", "").replace("_plugin", "")
    remove_file(f"{module}/_{name}.py")
    remove_file(f"{module}/_tests/test_{name}.py")
    logger.debug(f"removing {module}/_{name}.py")
    {% endif %}
    {% endfor %}


if __name__ == "__main__":
    move_docs_files("{{cookiecutter.docs_tool}}", DOCS_FILES_BY_TOOL, DOCS_SOURCES)
    remove_temp_folders(ALL_TEMP_FOLDERS)
    remove_unrequested_plugin_examples()

    print("""
Your plugin template is ready!  Next steps:

1. `cd` into your new directory and initialize a git repo
   (this is also important for version control!)

     cd {{ cookiecutter.plugin_name }}
     git init -b main
     git add .
     git commit -m 'initial commit'

2. Create a github repository with the name '{{ cookiecutter.plugin_name }}':
   https://github.com/new

3. Add your newly created github repo as a remote and push:

     git remote add origin https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.plugin_name }}.git
     git push -u origin main

4. Read the README for more info: https://github.com/napari/cookiecutter-napari-plugin
"""
    )
