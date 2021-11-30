"""
This module is an example of a barebones writer plugin for napari

It implements the Writer specification.
see: https://napari.org/plugins/stable/npe2_manifest_specification.html

Replace code below according to your needs.
"""
from __future__ import annotations
from typing import List
from numpy.typing import ArrayLike


def write_single_image(path: str, data: ArrayLike):
    pass


def write_multiple(path: str, data: List[ArrayLike], layer_types: List[str]):
    pass
