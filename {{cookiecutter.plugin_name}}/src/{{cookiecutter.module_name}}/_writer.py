"""
This module is an example of a barebones writer plugin for napari.

It implements the Writer specification.
see: https://napari.org/stable/plugins/guides.html?#writers

Replace code below according to your needs.
"""
from __future__ import annotations

from typing import TYPE_CHECKING, Any, List, Sequence, Tuple, Union

if TYPE_CHECKING:
    DataType = Union[Any, Sequence[Any]]
    FullLayerData = Tuple[DataType, dict, str]


def write_single_image(path: str, data: Any, meta: dict) -> List[str]:
    """Writes a single image layer.
    
    Parameters
    ----------
    path : str
           A string path indicating where to save the image file.
    data : The layer data
           The `.data` attribute from the napari layer.
    meta : dict
           A dictionary containing all other attributes from the napari layer
           (excluding the `.data` layer attribute).

    Returns
    -------
    [path] : A list containing the string path to the saved file.
    """

    # implement your writer logic here ...

    # return path to any file(s) that were successfully written
    return [path]


def write_multiple(path: str, data: List[FullLayerData]) -> List[str]:
    """Writes multiple layers of different types.
    
    Parameters
    ----------
    path : str
           A string path indicating where to save the image file.
    data : A layer tuple.
           Tuple contains three elements: (data, kwargs, layer_type)
           `data` is the layer data
           `kwargs` is a dictionary of keyword arguments
           `layer_type` is a string, eg: "image", "labels", "surface", etc.

    Returns
    -------
    [path] : A list containing multiple string paths to the saved files.
    """

    # implement your writer logic here ...

    # return path to any file(s) that were successfully written
    return [path]
