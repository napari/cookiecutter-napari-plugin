"""
This module is an example of a barebones plugin, using imageio.imread.

It implements the ``napari_get_reader`` hook specification, (to create
a reader plugin) but your plugin may choose to implement any of the hook
specifications offered by napari.  Replace code below depending on the
hook specification you want to implement.

See https://napari.org/docs/plugins/for_plugin_developers.html for more.
"""
import imageio
import numpy as np

from napari_plugin_engine import napari_hook_implementation

# ## for optional type hints only, otherwise you can delete/ignore this stuff ####

from typing import List, Optional, Union, Any, Tuple, Dict, Callable

FullLayerData = Tuple[Any, Dict, str]
LayerData = Union[Tuple[Any], Tuple[Any, Dict], FullLayerData]
PathLike = Union[str, List[str]]
ReaderFunction = Callable[[PathLike], List[LayerData]]
WriterFunction = Callable[[str, List[FullLayerData]], List[str]]

# ## End type hint stuff. ########################################################


IMAGEIO_EXTENSIONS = tuple(set(x for f in imageio.formats for x in f.extensions))


@napari_hook_implementation
def napari_get_reader(path: PathLike) -> Optional[ReaderFunction]:
    """A basic implementation of the napari_get_reader hook specification."""
    if isinstance(path, list):
        # reader plugins may be handed single path, or a list of paths.
        # if it is a list, it is assumed to be an image stack...
        # so we are only going to look at the first file.
        path = path[0]
    if not path.endswith(IMAGEIO_EXTENSIONS):
        # if we know we cannot read the file, we immediately return None.
        return None
    # otherwise we return the *function* that can read ``path``.
    return reader_function


def reader_function(path: PathLike) -> List[LayerData]:
    """Take a path or list of paths and return a list of LayerData tuples."""
    paths = [path] if isinstance(path, str) else path
    # stack a list of strings, but also works for a single path string
    data = np.squeeze(np.stack([imageio.imread(_path) for _path in paths]))
    # Readers are expected to return data as a list of tuples, where each tuple
    # is (data, [meta_dict, [layer_type]])
    meta = {}  # optional kwargs for the corresponding viewer.add_* method
    return [(data, meta)]
