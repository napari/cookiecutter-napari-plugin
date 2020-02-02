# Publish a Plugin

There are several ways to publish a [napari] plugin.

Essentially napari plugins are not different from any other Python Package, so
you may want to create a distribution and submit it to the Python Package Index
([PyPI]).

By doing so, enables your users to easily install via ``easy-install`` or
``pip``.

## Python Package Index

Submitting to [PyPI] that includes the following steps:

- Configuring your plugin (which is already covered in this template)
- Creating a distribution for your project
- Uploading your napari plugin to PyPI

Please see the official [Python Packaging User Guide] for detailed information.

## napari Organization

If you plan on submitting your plugin to the [napari organization] you need
to meet the following requirements:

- PyPI presence with a setup.py that contains a license, napari-
  prefixed, version number, authors, short and long description.
- a tox.ini for running tests using tox.
- a README describing how to use the plugin and on which platforms
  it runs.
- a LICENSE file or equivalent containing the licensing information,
  with matching info in setup.py.
- an issue tracker unless you rather want to use the core napari
  issue tracker.

Please see the official guidelines at [Submit a Plugin].

  [napari organization]: https://github.com/napari/
  [Submit a Plugin]: https://napari.org/latest/contributing.html#submit-a-plugin-co-develop-napari
  [napari]: https://github.com/napari/napari
  [PyPI]: https://pypi.org/project
  [Python Packaging User Guide]: https://python-packaging-user-guide.readthedocs.io/en/latest/distributing.html
