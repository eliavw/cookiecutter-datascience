Cookiecutter-datascience
========================

Cookiecutter template for datascience projects.

Usage
-----
To start a new project from this cookiecutter, install [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) _(duh)_ and then do;

```bash
cookiecutter gh:eliavw/cookiecutter-datascience
``` 

Future work
-----------

This is still a work in progress and will likely never be finished. However, it can be improved. Some ideas for new, extra features are;

- CI on github
- Edit `setup.py` so that it parses `dependencies-deploy.yaml` and adds them to `setup.cfg` automatically. Also, as a policy adopt pip first, conda second. For python packages, everything has to be in pip anyways.
- Auto-generate API docs from docstrings
- Unittest docs and code style
- Generate tests from notebooks
- git hooks

Unintended side-effect
----------------------

_This_ repo is also basically an example of how _you_ can also make your own cookiecutter!
