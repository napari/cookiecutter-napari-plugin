# User Guide

## What is Cookiecutter?

[Cookiecutter] is a command-line utility that creates projects from **cookiecutters** (project
templates), e.g. creating a Python package project from a Python package project template.

## Installation

Cookiecutter is available on [PyPI]. Use ``pip`` to download and install:

```no-highlight
$ pip install cookiecutter
```

## Usage

You can generate a new project from a template by using the following command:

```no-highlight
$ cookiecutter https://github.com/napari/cookiecutter-napari-plugin
```

This will not only ``git clone`` the template but also start the generation process.

## Template Variables

Each Cookiecutter template uses variables, which are specified in the template, that
it replaces in all of the directory and file names, but also in text such as source code
or markdown formats.

### Plugin Details

Cookiecutter prompts you for information regarding your plugin based on aforementioned variables:

```no-highlight
full_name [Napari Developer]: Ramon y Cajal
email [yourname@example.com]: ramon@cajal.es
github_username_or_organization [githubuser]: neuronz52
plugin_name [napari-foobar]: growth-cone-finder
module_name [growth_cone_finder]: growth_cone_finder
short_description [A simple plugin to use with napari]:
version [0.1.0]:
minimum_napari_version [None]: 0.3.0
```

The values in the square brackets (f.i. ``[napari-foobar]``) are defaults for the according variables.

## Project Generation

Once you answered to the questions, Cookiecutter renders the the project:

```no-highlight
napari-growth-cone-finder/
├── LICENSE
├── README.md
├── napari_growth_cone_finder.py
├── setup.py
├── tests
│   ├── conftest.py
│   └── test_growth_cone_finder.py
└── tox.ini
```

create repo on github (don't worry about git ignore or readme)

pip install cookiecutter
cookiecutter https://github.com/napari/cookiecutter-napari-plugin

cd into your directory
git init
git add .
git commit -m 'initial commit'

git remote add origin https://github.com/tlambert03/napari-ndtiffs.git
git push -u origin master

testing locally:
...

There you go - you just created a minimal napari plugin!

[Cookiecutter]: https://github.com/audreyr/cookiecutter
[PyPI]: https://pypi.org/project/cookiecutter
