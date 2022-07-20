# {{cookiecutter.plugin_name}}

[![License {{cookiecutter.license}}](https://img.shields.io/pypi/l/{{cookiecutter.plugin_name}}.svg?color=green)](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/{{cookiecutter.plugin_name}}.svg?color=green)](https://pypi.org/project/{{cookiecutter.plugin_name}})
[![Python Version](https://img.shields.io/pypi/pyversions/{{cookiecutter.plugin_name}}.svg?color=green)](https://python.org)
[![tests](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/workflows/tests/badge.svg)](https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/actions)
[![codecov](https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/branch/main/graph/badge.svg)](https://codecov.io/gh/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}})
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/{{cookiecutter.plugin_name}})](https://napari-hub.org/plugins/{{cookiecutter.plugin_name}})

{{cookiecutter.short_description}}

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `{{cookiecutter.plugin_name}}` via [pip]:

    pip install {{cookiecutter.plugin_name}}


{% if cookiecutter.github_repository_url != 'provide later' %}
To install latest development version :

    pip install git+https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}.git
{% endif %}

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [{{cookiecutter.license}}] license,
"{{cookiecutter.plugin_name}}" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
{% if cookiecutter.github_repository_url != 'provide later' %}
[file an issue]: https://github.com/{{cookiecutter.github_username_or_organization}}/{{cookiecutter.plugin_name}}/issues
{% endif %}
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
