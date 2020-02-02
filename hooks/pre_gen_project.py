#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pre_gen_project")

PLUGIN_REGEX = r"^(?!napari)[-_a-zA-Z][-_a-zA-Z0-9]+$"
MODULE_REGEX = r"^[a-z][_a-z0-9]+$"

plugin_name = "{{cookiecutter.plugin_name}}"
module_name = "{{cookiecutter.module_name}}"

if not re.match(PLUGIN_REGEX, plugin_name):
    logger.error(
        f'Invalid value for plugin_name "{plugin_name}"'
        '\n\tPlease do not prepend plugin_name with "napari"!'
    )
    sys.exit(1)

if not re.match(MODULE_REGEX, module_name):
    link = "https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
    logger.error("Module name should be pep-8 compliant.")
    logger.error("  More info: {}".format(link))
    sys.exit(1)
