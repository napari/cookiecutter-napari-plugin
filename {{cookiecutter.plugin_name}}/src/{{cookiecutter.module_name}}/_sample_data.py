"""
This module is an example of a barebones sample data provider for napari.

It implements the "sample data" specification.
see: https://napari.org/plugins/guides.html?highlight=sample_data#sample-data

Replace code below according to your needs.
"""
from __future__ import annotations
import numpy


def make_sample_data():
    """Generates an image"""
    return numpy.random.rand(512, 512)
