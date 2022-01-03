from {{cookiecutter.module_name}} import ExampleQWidget, example_magic_widget
import numpy as np
import pytest

@pytest.fixture
def random_im():
    return np.random.random((100, 100))

def test_example_q_widget(make_napari_viewer, capsys, random_im):
    viewer = make_napari_viewer()
    viewer.add_image(random_im)
    my_widget = ExampleQWidget(viewer)
    my_widget._on_click()

    captured = capsys.readouterr()
    assert captured.out == "napari has 1 layers\n"
    
def test_example_magic_widget(make_napari_viewer, capsys, random_im):
    viewer = make_napari_viewer()
    layer = viewer.add_image(random_im)
    my_widget = example_magic_widget()

    my_widget(viewer.layers[0])
    captured = capsys.readouterr()
    assert captured.out == f"you have selected {layer}\n"
