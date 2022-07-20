# napari Plugin Prompt Reference

When you first run cookiecutter to build a napari plugin, you will be prompted
for some configuration options. Your answers to these prompts will determine
some aspects of your plugin package including its name, versioning behaviour,
license, etc. None of these configuration options are set in stone - you
can always change these later, but it may require some effort.

This document details what each of the prompts is asking, what the effect
of your choice will be on your package directory/plugin, and any potential
pitfalls of selecting one option over another.

**Note: ** Many of these configuration options will also affect how your plugin
appears on the [napari hub](https://www.napari-hub.org/). If you're planning
on publishing your plugin to PyPI (and by extension, the hub), you can refer
to [this document](https://github.com/chanzuckerberg/napari-hub/blob/main/docs/customizing-plugin-listing.md) for detailed documentation on customizing your listing.

## full_name

This is the name of the main author of this plugin, and will appear in your
`setup.cfg` file. If you publish your plugin to PyPI, this name will also be listed
in the author metadata field.

## email

This is your preferred contact email address and will appear in your `setup.cfg`
file. If you publish your plugin to PyPI, this contact email address wil be
listed next to the author's name.

## github_username_or_organization

This is the GitHub username under whose account the GitHub repository for the
plugin will be hosted. This username will be used to create the GitHub url
for this plugin and will appear as part of the `url` field in `setup.cfg`.

This username could be your personal username or the organization under which
you plan to host the plugin on GitHub. If you do not wish to provide a username,
simply press `Enter` at this prompt, and choose `provide later` at the
`github_repository_url` prompt - this will omit the `url` field in `setup.cfg`
entirely, and you may add it later if you wish.

## plugin_name

This is the desired name for your napari plugin, and will also be the name
of the Python package directory we create for you. The plugin name you choose
will be listed in `setup.cfg` under the `name` field, as well as under
`[options.entry_points]`. If you publish your package to PyPI, users will be able
to install your package using

```
pip install plugin_name
```

The convention for these packages is that they should have short, all-lowercase
names, with hyphens preferred over underscores for separating words.

## github_repository_url

This will be the code repository link that is stored in the `url` field in
`setup.cfg`. The default option is generated using your `github_username_or_organization` and `plugin_name`.

Choose `provide later` at this prompt if the default generated url is incorrect,
or if you do not wish to provide a url at all. You can then add this link to your
`setup.cfg` later, under the `url` field.

## module_name

This is the name of the Python module where the code for your plugin will live.
We create a folder with this name inside the top level directory of your plugin,
and populate it with code templates.

This module will also be added as the entry point to your plugin in `setup.cfg`.
This is how napari discovers plugins on launch.

## display_name

User-facing text to display as the name of this plugin. It should be 3-40
characters long. It will be listed in `napari.yaml` under the `display_name`
field.

## short_description

This should be a short description of what your plugin does. It will be listed
in `setup.cfg` under the `description` field. If you publish your plugin to PyPI,
this description will also be listed alongside your package name in search results.

## include_reader_plugin

Choosing `"y"` for this prompt will create an example reader implementation
inside your plugin's module in the file `_reader.py`. You can then edit the code in this
file to achieve the reading functionality you want. For more information on
readers see the [specification reference][reader-spec].

## include_writer_plugin

Choosing `"y"` for this prompt will create an example writer hook
implementation inside your plugin's module in the file `_writer.py`. You can
then edit the code in this file to achieve the writing functionality you want.
For more information on writers see the
[specification reference][writer-spec].

## include_sample_data_plugin

Choosing `"y"` for this prompt will create an example sample-data provider
implementation inside your plugin's module in the file `_sample_data.py`.
For more information see the [specification reference][sample-data-spec].

## include_widget_plugin

Choosing `"y"` for this prompt will create an example widget contribution
inside your plugin's module in the file `_widget.py`. You can then edit
the code in this file to achieve the dock widget functionality you want. For
more information on dock widgets see the
[specification reference][widget-spec].

## use_git_tags_for_versioning

The default for this prompt is `"n"`. If you choose `"n"` for this prompt, you
will have to manually manage your version numbers when you create new releases
of your package. You can do this in `setup.cfg` under the `version` field (you
will also need to update the version string wherever else you may have used it
in your package, such as in `__init__.py`). Choosing `"n"` at this prompt will
add `version = 0.0.1` to your `setup.cfg`.

If you choose `"y"` for this prompt, your package will be set up to have
[`setuptools_scm`](https://github.com/pypa/setuptools_scm) manage versions for
you based on your git tags. See the
[readme](https://github.com/napari/cookiecutter-napari-plugin#automatic-deployment-and-version-management)
for details.

This option typically requires the least effort to manage versioning for your
package, and will prevent errors with manually managed version strings going out
of sync with your package metadata. The main downside is that your users will
not be able to install directly from a github release asset, and will need to
have git installed if they want to directly install from a git repository.
(This does _not_, however, affect the standard method of installing with `pip`, or
installing from a pre-packaged wheel file.)

```{note}
In order to use this option, you must run `git init` once in
your package's root directory.
```

## license

This prompt allows you to choose from a variety of open source licensing options
for your plugin. Choosing any of the options will lead to a boilerplate `LICENSE`
file being added to the root of your plugin directory, as well as the [SPDX identifier](https://spdx.org/licenses/)
for that license being listed in your `setup.cfg` under the `license` field.

License options include: [BSD-3], [MIT], [MPL v2.0], [Apache v2.0], [GNU GPL v3.0], or [GNU LGPL v3.0]

[spec]: https://napari.org/stable/plugins/manifest.html
[reader-spec]: https://napari.org/stable/plugins/contributions.html#contributions-readers
[writer-spec]: https://napari.org/stable/plugins/contributions.html#contributions-writers
[theme-spec]: https://napari.org/stable/plugins/contributions.html#contributions-themes
[widget-spec]: https://napari.org/stable/plugins/contributions.html#contributions-widgets
[sample-data-spec]: https://napari.org/stable/plugins/contributions.html#contributions-sample-data
[glob pattern]: https://en.wikipedia.org/wiki/Glob_(programming)
[mit]: http://opensource.org/licenses/MIT
[mpl v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[bsd-3]: http://opensource.org/licenses/BSD-3-Clause
[gnu gpl v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[gnu lgpl v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
