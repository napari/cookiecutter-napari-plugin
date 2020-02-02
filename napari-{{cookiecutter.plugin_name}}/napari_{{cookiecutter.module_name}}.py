# -*- coding: utf-8 -*-

from napari.plugins import hookimpl
from napari.plugins.hookspecs import LayerData, ReaderFunction, Optional, List


# type annotations here are optional
# see napari hookspecs for details on hooks that can be implemented


def my_tiff_reader(path: str) -> List[LayerData]:
    return [(None, {"path": path})]


@hookimpl
def napari_get_reader(path: str) -> Optional[ReaderFunction]:
    if path.endswith(".tif"):
        return my_tiff_reader
