# cookiecutter-datascience

Cookiecutter template for datascience

1 Development workflows
=======================

1.1 Start project
-----------------

Using the power of both `PyScaffold` and `cookiecutter` templates, this single command provides a pretty solid starting point for any new project.

```bash
putup project-name --cookiecutter gh:eliavw/cookiecutter-datascience --markdown --travis
```

1.2 git
-------

Version control goes without saying.

1.3 CI
------

Do not allow yourself to proceed without at least accumulating some tests. Therefore, we've set out to intigrate CI (i.e. Travis) right from the start.

1.4 Conda environments
----------------------
This is a personal preference. This cookiecutter is set up to accomodate conda environments, since they are quite useful for datascience projects. The main message would be `for local dependency/package managment, we use conda and nothing else`


2 Distribution workflows
========================

This part is about publishing your project on PyPi.

2.1 Pypi
--------

Follow these steps

2.2 Docs
--------
Every project needs documentation.

2.3 Docker
----------

2.4 Singularity
---------------
