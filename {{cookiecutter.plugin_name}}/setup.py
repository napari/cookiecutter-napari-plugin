#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup

{% if cookiecutter.plugin_name == "foo-bar" %}
# extracted because it breaks testing of this cookiecutter template
use_scm = False
{% else %}
# https://github.com/pypa/setuptools_scm
use_scm = {"write_to": "{{cookiecutter.module_name}}/_version.py"}
{% endif %}
setup(
    use_scm_version=use_scm,
)
