# -*- coding: utf-8 -*-

from napari_{{cookiecutter.module_name}} import napari_get_reader


# # the best test here would to use tempfile.NamedTemporaryFile
# def test_reader():
#     from tempfile import NamedTemporaryFile
#     import numpy as np
#
#     # use your own `.ext` here
#     with NamedTemporaryFile(suffix='.ext', delete=False) as tmp:
#         out_data = np.random.rand(20, 20)
#         # write_data_to_file(tmp.name, out_data)
#         reader = napari_get_reader(tmp)
#         in_data = reader(tmp.name)
#         assert np.allclose(out_data, in_data)


def test_get_reader_hit():
    reader = napari_get_reader('fake.tif')
    assert reader is not None
    assert callable(reader)


def test_get_reader_with_list():
    # a better test here would use real data
    reader = napari_get_reader(['fake.tif'])
    assert reader is not None
    assert callable(reader)


def test_get_reader_pass():
    reader = napari_get_reader('fake.file')
    assert reader is None
