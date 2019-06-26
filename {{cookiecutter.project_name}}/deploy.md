Deployment Information
======================

We use git for versioning and conda for package managment.

Version Control
---------------

Create an empty repository on github, then;

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
