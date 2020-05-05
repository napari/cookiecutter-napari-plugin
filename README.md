# cookiecutter-napari-plugin

Minimal [Cookiecutter] template for authoring [napari] plugins.

> This template requires [Cookiecutter 1.4.0 "Shortbread"][Shortbread] or
> higher

## Features

- Installable [PyPI] package featuring a `setup.py`
- [tox] test suite, testing various python versions and platforms.
- `README.md` file that contains useful information about your plugin
- Continuous integration configuration for [github actions] that handles testing
  and deployment of tagged releases
- git-tag-based version management with [setuptools_scm]
- Optional documentation with either [Sphinx] or [MkDocs]
- Choose from several licenses, including [BSD-3], [MIT], [MPL v2.0], [Apache
  v2.0], [GNU GPL v3.0], or [GNU LGPL v3.0]

## Getting Started

### Create your plugin package

Install [Cookiecutter] and generate a new napari plugin project:

```bash
pip install cookiecutter
cookiecutter https://github.com/napari/cookiecutter-napari-plugin
```

Cookiecutter prompts you for information regarding your plugin
(A new folder will be created in your current working directory):

```no-highlight
full_name [Napari Developer]: Ramon y Cajal
email [yourname@example.com]: ramon@cajal.es
github_username [githubuser]: neuronz52
plugin_name [foobar]: growth-cone-finder
module_name [growth_cone_finder]: growth_cone_finder
short_description [A simple plugin to use with napari]:
Select docs_tool:
1 - mkdocs
2 - sphinx
3 - none
Choose from 1, 2, 3 [1]: 3
Select license:
1 - BSD-3
2 - MIT
3 - Mozilla Public License 2.0
4 - Apache Software License 2.0
5 - GNU LGPL v3.0
6 - GNU GPL v3.0
Choose from 1, 2, 3, 4, 5, 6 (1, 2, 3, 4, 5, 6) [1]:
INFO:post_gen_project:Moving files for mkdocs.
```

You just created a minimal napari plugin, complete with tests
and ready for automatic deployment!

```no-highlight
napari-growth-cone-finder/
│
├── .github
│   └── workflows
│      └── test_and_deploy.yml
├── docs
│   └── index.md
├── LICENSE
├── MANIFEST.in
├── mkdocs.yml
├── napari_growth_cone_finder
│   ├── __init__.py
│   ├── _tests
│   │   ├── __init__.py
│   │   └── test_grown_cone_finder.py
│   └── growth_cone_finder.py
├── README.md
├── requirements.txt
├── setup.py
└── tox.ini
```

### Upload it to github

1. Create a [new github repository]
2. Initialize git in your new package:

    ```bash
    cd napari-growth-cone-finder
    git init
    git add .
    git commit -m 'initial commit'
    ```

3. Add your newly created github repo as a remote and push:

    ```bash
    # here, continuing with the example above...
    # but replace with your own username and repo name

    git remote add origin https://github.com/neuronz52/napari-growth-cone-finder.git
    git push -u origin master
    ```

The repository should already be setup to run your tests each time you
push an update (configuration is in `.github/workflows/test_and_deploy.yml`).
You can monitor them in the "Actions" tab of your github repository.

### Set up automatic deployments

Your new package is also nearly ready to automatically deploy to [PyPI]
(whenever you create a tagged release), so that your users can simply `pip
install` your package. You just need to create an [API token to authenticate
with PyPi](https://pypi.org/help/#apitoken), and then add it to your github
repository:

1. If you don't already have one, [create an
   account](https://pypi.org/account/register/) at [PyPI]
2. Verify your email address with PyPI, (if you haven't already)
3. Generate an [API token](https://pypi.org/help/#apitoken) at PyPi: In your
   [account settings](https://pypi.org/manage/account/) go to the API tokens
   section and select "Add API token". Make sure to copy it somewhere safe!
4. [Create a new encrypted
   secret](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets#creating-encrypted-secrets)"
   in your github repository with the name "TWINE_API_KEY", and paste in your
   API token.

### Deployment and version management

You are now setup for deployment!  Each time you want to deploy a new version,
you just need to create a tagged commit, and push it to your master branch on
github.  Your package is set up to use
[setuptools_scm](https://github.com/pypa/setuptools_scm) for version management,
meaning you don't need to hard-code your version anywhere in your package.  It
will be inferred from the tag each time you release.

```bash
# the tag will be used as the version string for your package
# make it meaningful: https://semver.org/
git tag -a v0.1.0 -m "v0.1.0"

# make sure to use follow-tags so that the tag also gets pushed to github
git push --follow-tags
```

> Note: as of git 2.4.1, you can set `follow-tags` as default with
> `config --global push.followTags true`

### Testing locally

You can run your tests locally using [tox], just by entering `tox` on the
command line. If you are using `conda` for environment management, you may wish
to `pip install tox-conda` to make tox play nice with conda.



## Resources

Please consult the [napari plugin
docs](https://napari.org/docs/plugins/index.html) for more information on
how to create a plugin.

## Issues

If you encounter any problems with this cookiecutter template, please [file an
issue] along with a detailed description.

## License

Distributed under the terms of the [BSD-3] license, `cookiecutter-napari-plugin`
is free and open source software.

[napari organization]: https://github.com/napari/
[gitter_badge]: https://badges.gitter.im/Join%20Chat.svg
[gitter]: https://gitter.im/napari/cookiecutter-napari-plugin?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge (Join Chat on Gitter.im)
[travis_badge]: https://travis-ci.org/napari/cookiecutter-napari-plugin.svg?branch=master
[travis]: https://travis-ci.org/napari/cookiecutter-napari-plugin (See Build Status on Travis CI)
[docs_badge]: https://readthedocs.org/projects/cookiecutter-napari-plugin/badge/?version=latest
[documentation]: https://cookiecutter-napari-plugin.readthedocs.io/en/latest/ (Documentation)
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[napari]: https://github.com/napari/napari
[PyPI]: https://pypi.org/
[tox]: https://tox.readthedocs.io/en/latest/
[file an issue]: https://github.com/napari/cookiecutter-napari-plugin/issues
[Sphinx]: http://sphinx-doc.org/
[MkDocs]: http://www.mkdocs.org/
[MIT]: http://opensource.org/licenses/MIT
[MPL v2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache v2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Travis CI]: https://travis-ci.com/
[AppVeyor]: http://www.appveyor.com/
[PyPA Code of Conduct]: https://www.pypa.io/en/latest/code-of-conduct/
[Shortbread]: https://github.com/audreyr/cookiecutter/releases/tag/1.4.0
[osi_certified]: https://opensource.org/trademarks/osi-certified/web/osi-certified-120x100.png
[OSI]: https://opensource.org/
[github actions]: https://github.com/features/actions
[new github repository]: https://help.github.com/en/github/getting-started-with-github/create-a-repo
[setuptools_scm]: https://github.com/pypa/setuptools_scm