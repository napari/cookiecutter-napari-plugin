# -*- coding: utf-8 -*-

from napari_{{cookiecutter.module_name}} import napari_get_reader


# # tmp_path is a pytest fixture
# def test_reader(tmp_path):
#     """An example of how you might test your plugin..."""
#     import numpy as np
#     # use your own `.ext` here
#     my_test_file = tmp_path / "myfile.ext"

#     # write some data
#     out_data = np.random.rand(20, 20)
#     write_data_to_file(my_test_file, out_data)

#     # try to read it back in
#     reader = napari_get_reader(my_test_file)
#     in_data = reader(my_test_file)

#     assert np.allclose(out_data, in_data)


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
