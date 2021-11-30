"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/plugins/stable/npe2_manifest_specification.html

Replace code below according to your needs.
"""
from __future__ import annotations
import numpy
from numpy.typing import ArrayLike


def make_sample_data() -> ArrayLike:
    """Generates an image"""
    return numpy.random.rand(512, 512)
