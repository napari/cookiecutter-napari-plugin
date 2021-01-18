#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


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
    name='{{cookiecutter.plugin_name}}',
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    license='{{cookiecutter.license}}',
    url='https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.plugin_name}}',
    description='{{cookiecutter.short_description}}',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=requirements,
    use_scm_version=use_scm,
    setup_requires=['setuptools_scm'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Framework :: napari',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
        {% if cookiecutter.license == "MIT" -%}
        'License :: OSI Approved :: MIT License',
        {%- elif cookiecutter.license == "BSD-3" -%}
        'License :: OSI Approved :: BSD License',
        {%- elif cookiecutter.license == "GNU GPL v3.0" -%}
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        {%- elif cookiecutter.license == "Apache Software License 2.0" -%}
        'License :: OSI Approved :: Apache Software License',
        {%- elif cookiecutter.license == "Mozilla Public License 2.0" -%}
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        {%- endif %}
    ],
    entry_points={
        'napari.plugin': [
            '{{cookiecutter.plugin_name}} = {{cookiecutter.module_name}}',
        ],
    },
)
