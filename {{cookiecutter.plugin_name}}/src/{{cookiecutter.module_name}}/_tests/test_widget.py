import numpy as np

from {{cookiecutter.module_name}}._widget import (
    ExampleQWidget,
    ImageThreshold,
    example_function_widget,
    example_magic_widget,
)


def test_example_function_widget():
    # because our "widget" is a pure function, we can call it and
    # test it independently of napari
    im_data = np.random.random((100, 100))
    thresholded = example_function_widget(im_data)
    assert thresholded.shape == im_data.shape
    # etc.


# make_napari_viewer is a pytest fixture that returns a napari viewer object
# you don't need to import it, as long as napari is installed
# in your testing environment
def test_example_magic_widget(make_napari_viewer):
    viewer = make_napari_viewer()
    layer = viewer.add_image(np.random.random((100, 100)))

    # our widget will be a MagicFactory or FunctionGui instance
    my_widget = example_magic_widget()

    # if we "call" this object, it'll execute our function
    thresholded = my_widget(viewer.layers[0], 0.5)
    assert thresholded.shape == layer.data.shape
    # etc.


def test_image_threshold_widget(make_napari_viewer):
    viewer = make_napari_viewer()
    layer = viewer.add_image(np.random.random((100, 100)))
    my_widget = ImageThreshold(viewer)

    # because we saved our widgets as attributes of the container
    # we can set their values without having to "interact" with the viewer
    my_widget._image_layer_combo.value = layer
    my_widget._threshold_slider.value = 0.5

    # this allows us to run our functions directly and ensure
    # correct results
    my_widget._threshold_im()
    assert len(viewer.layers) == 2


# capsys is a pytest fixture that captures stdout and stderr output streams
def test_example_q_widget(make_napari_viewer, capsys):
    # make viewer and add an image layer using our fixture
    viewer = make_napari_viewer()
    viewer.add_image(np.random.random((100, 100)))

    # create our widget, passing in the viewer
    my_widget = ExampleQWidget(viewer)

    # call our widget method
    my_widget._on_click()

    # read captured output and check that it's as we expected
    captured = capsys.readouterr()
    assert captured.out == "napari has 1 layers\n"
