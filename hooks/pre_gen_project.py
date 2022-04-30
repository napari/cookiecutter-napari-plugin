#!/usr/bin/env python

import logging
import re
import sys

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("pre_gen_project")

if not re.match(r"^[a-z][_a-z0-9]+$", "{{cookiecutter.module_name}}"):
    link = "https://www.python.org/dev/peps/pep-0008/#package-and-module-names"
    logger.error("Module name should be pep-8 compliant.")
    logger.error(f"  More info: {link}")
    sys.exit(1)

if re.match(r"_", "{{cookiecutter.plugin_name}}"):
    logger.error("PyPI.org and pip discourage package names with underscores.")
    sys.exit(1)
