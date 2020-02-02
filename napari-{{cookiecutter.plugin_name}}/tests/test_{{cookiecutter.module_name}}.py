# -*- coding: utf-8 -*-

from napari_{{cookiecutter.module_name}} import napari_get_reader


def test_get_reader_hit():
    reader = napari_get_reader('fake.tif')
    assert reader is not None
    assert callable(reader)


def test_get_reader_pass():
    reader = napari_get_reader('fake.file')
    assert reader is None
