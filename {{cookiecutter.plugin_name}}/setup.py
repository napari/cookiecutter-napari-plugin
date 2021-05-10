#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup


# Add your dependencies in requirements.txt
# Note: you can add test-specific requirements in tox.ini
requirements = []
with open('requirements.txt') as f:
    for line in f:
        stripped = line.split("#")[0].strip()
        if len(stripped) > 0:
            requirements.append(stripped)

{% if cookiecutter.plugin_name == "foo-bar" %}
# extracted because it breaks testing of this cookiecutter template
use_scm = False
{% else %}
# https://github.com/pypa/setuptools_scm
use_scm = {"write_to": "{{cookiecutter.module_name}}/_version.py"}
{% endif %}
setup(
    install_requires=requirements,
    use_scm_version=use_scm,
)
