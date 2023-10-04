import numpy as np

from {{cookiecutter.module_name}} import example_function_widget, example_magic_widget, ExampleQWidget




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
