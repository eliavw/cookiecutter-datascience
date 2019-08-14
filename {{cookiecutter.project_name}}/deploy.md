# {{cookiecutter.project_name}}

Deployment information.

1 Development workflows
=======================

1.1 Start project
-----------------

Using the power of `cookiecutter`, this single command provides a pretty solid starting point for any new project.

```bash
cookiecutter gh:{{cookiecutter.github_username}}/cookiecutter-datascience
```

1.2 git
-------

Version control goes without saying. For the local repository, do;

```bash
git init
git add .
git commit -m "First commit"
```

or alternatively, the one-liner;

```bash
git init; git add .; git commit -m "First commit";
```

For the remote repository, do;

```bash
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git
git remote -v
git push origin master
```

And that's it for git.

1.3 Conda Environments
----------------------

### Introduction

This cookiecutter is set up for optimal use with [conda](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf), for **local dependency managment**. The takeaway is this; _for local dependency managment, we rely on conda and nothing else._

Note that this has nothing to do with **remote dependency managment**. This is what you need to take care of when preparing a _release_ of your code which goes via [PyPi](https://pypi.org/) or alternatives. We treat that as an independent problem. Mixing remote and local dependency managment tends to add complexity instead of removing it.

### Workflow

To create our default environment, do:

```bash
conda env create -f dependencies-deploy.yaml -n {{cookiecutter.project_name}}
```

To additionally add the packages which are relevant for the development phase, do:

```bash
conda activate {{cookiecutter.project_name}}
conda env update -n {{cookiecutter.project_name}} -f dependencies-develop.yaml
```

1.4 CI (Travis)
---------------

Do not allow yourself to proceed without at least accumulating some tests. Therefore, we've set out to intigrate CI (i.e. Travis) right from the start.

Follow these steps:

1. Go to https://travis-ci.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}
2. See if it ran.

**Note:** The tests depend on our **local dependecy managment**. Why? Because we have full control of the Travis servers running our tests. Therefore, we can simply treat it as a computer we'd control. We only need to fall back on remote dependency managment if other people need to get our code up and running, without our intervention.


1.4 Conda environments
----------------------



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



Deployment Information
======================

We use git for versioning and conda for package managment.

Version Control
---------------

First, create an empty repository on github, e.g.: `eliavw/{{cookiecutter.project_name}}`.

Then, add the following lines to `.gitignore`,

```bash
.ipynb_checkpoints
```

to ignore the useless checkpoint folders.


```bash
git init
git add .
git commit -m "First commit"
git remote add origin git@github.com:eliavw/{{cookiecutter.project_name}}.git
git remote -v
git push origin master
```

Reproducibility
---------------

Environment made with conda. To make an environment;

```bash
conda create --name {{cookiecutter.project_name}} python=3.7 ipykernel
```

### Export
This environment can be exported to a `.yml` file through the following command:

```bash
conda env export > environment.yml
```

Which creates the `.yml` file present in the root dir.


### Load
To recreate this environment, it suffices to run;

```bash
conda env create -f environment.yml -n {{cookiecutter.project_name}} 
```

Which presupposes a miniconda on your own machine.

### Add kernel to Jupyter

To add this python environment to the list of Jupyter environments, do the following. 
```bash
source activate {{cookiecutter.project_name}}
python -m ipykernel install --user --name {{cookiecutter.project_name}} --display-name "{{cookiecutter.project_name}}"
```

_N.b.: This requires ipykernel to be installed in the environment._

Dependency Managment
--------------------

For a pip install, you also need some kind of reproducibility. What matters there is the fact that you need to list your abstract dependencies. This needs to be done in the `setup.cfg` file.


Continuous Integration - Tests
------------------------------

Documentation
-------------

Install sphinx, if necessary. Obviously, no need to do this explicitly in your isolated environment, that will just bloat everything.

```bash
conda install sphinx
```

Then render the docs as

```bash
python setup.py docs
```

Publish
-------

To upload the final product to pip, first edit the `setup.cfg` file.
