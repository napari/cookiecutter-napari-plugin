# cookiecutter-napari-plugin

Minimal [Cookiecutter] template for authoring [napari] plugins that help
you to write better programs.

> This template requires [Cookiecutter 1.4.0 "Shortbread"][Shortbread] or
> higher

## Getting Started

Install [Cookiecutter] and generate a new napari plugin project:

```no-highlight
$ pip install cookiecutter
$ cookiecutter https://github.com/napari/cookiecutter-napari-plugin
```

Cookiecutter prompts you for information regarding your plugin:

```no-highlight
full_name [Napari Developer]: Ramon y Cajal
email [yourname@example.com]: ramon@cajal.es
github_username [githubuser]: neuronz52
plugin_name [foobar]: Growth Cone Finder
module_name [growth_cone_finder]: growth_cone_finder
short_description [A simple plugin to use with napari]:
version [0.1.0]:
napari_version [0.2.12]:
Select docs_tool:
1 - mkdocs
2 - sphinx
3 - none
Choose from 1, 2, 3 [1]: 1
Select license:
1 - MIT
2 - BSD-3
3 - GNU GPL v3.0
Choose from 1, 2, 3 [1]: 2
INFO:post_gen_project:Moving files for mkdocs.
```

There you go - you just created a minimal napari plugin:

```no-highlight
napari-growth_cone_finder/
├── LICENSE
├── README.rst
├── docs
│   └── index.md
├── mkdocs.yml
├── napari_growth_cone_finder.py
├── setup.py
├── tests
│   ├── conftest.py
│   └── test_growth_cone_finder.py
└── tox.ini
```

## Features

- Installable [PyPI] package featuring a `setup.py`.
- Test suite running [tox] and [napari] that makes sure your plugin is working
  as expected
- Working example code for a fixture, a cli option, as well as a napari.ini
  option
- Comprehensive `README.rst` file that contains useful information about your
  plugin
- Continuous integration configuration for [Travis CI] and [AppVeyor]
- Optional documentation with either [Sphinx] or [MkDocs]
- Choose from several licenses, such as [MIT], [BSD-3], [Apache v2.0], [GNU GPL
  v3.0], or [MPL v2.0]

## Requirements to Submit a Plugin

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

## Resources

Please consult the [napari] docs for more information on hooks at
[napari hook reference].

## Contribute

We welcome you to contribute to this project. Please visit the [documentation]
to get started!

## Issues

If you encounter any problems, please [file an issue] along with a
detailed description.

## License

Distributed under the terms of the [MIT license], cookiecutter napari
plugin is free and open source software.

  [napari organization]: https://github.com/napari/
  [gitter_badge]: https://badges.gitter.im/Join%20Chat.svg
  [gitter]: https://gitter.im/napari/cookiecutter-napari-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge (Join Chat on Gitter.im)
  [travis_badge]: https://travis-ci.org/napari/cookiecutter-napari-plugin.svg?branch=master
  [travis]: https://travis-ci.org/napari/cookiecutter-napari-plugin (See Build Status on Travis CI)
  [docs_badge]: https://readthedocs.org/projects/cookiecutter-napari-plugin/badge/?version=latest
  [documentation]: https://cookiecutter-napari-plugin.readthedocs.io/en/latest/ (Documentation)
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [napari]: https://github.com/napari/napari
  [PyPI]: https://pypi.org/project
  [tox]: https://tox.readthedocs.io/en/latest/
  [Submit a Plugin]: https://docs.napari.org/en/latest/contributing.html#submitting-plugins-to-napari
  [napari hook reference]: https://docs.napari.org/en/latest/writing_plugins.html#napari-hook-reference
  [MIT license]: http://opensource.org/licenses/MIT
  [file an issue]: https://github.com/napari/cookiecutter-napari-plugin/issues
  [Sphinx]: http://sphinx-doc.org/
  [MkDocs]: http://www.mkdocs.org/
  [MIT]: http://opensource.org/licenses/MIT
  [MPL v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
  [BSD-3]: http://opensource.org/licenses/BSD-3-Clause
  [GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
  [Apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
  [Travis CI]: https://travis-ci.com/
  [AppVeyor]: http://www.appveyor.com/
  [PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
  [Shortbread]: https://github.com/audreyr/cookiecutter/releases/tag/1.4.0
  [osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
  [OSI]: https://opensource.org/
