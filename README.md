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

This is still a work in progress and will likely never be finished. However, everything can always be done better. 

Some ideas for new, extra features are;

-[ ] Test: CI on github
-[ ] Test: Notebooks as integration tests
-[ ] DM: Edit `setup.py` so that it parses `dependencies-deploy.yaml` and adds them to `setup.cfg` automatically. Also, as a policy; adopt pip first, conda second. For python packages, everything has to be in pip anyways.
-[ ] Docs: Auto-generate API docs from docstrings
-[ ] Test: Unittest docs and code style


Side-effect
----------------------

_This_ repo is also basically an example of how _you_ can also make your own cookiecutter!
