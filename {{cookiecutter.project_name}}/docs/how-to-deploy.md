# Backend info

Development & deployment information for this project.

## Development Workflows

### Start Project with Cookiecutter

Using the power of [cookiecutter](https://cookiecutter.readthedocs.io/en/latest/), this single command provides a pretty solid starting point for any new project.

```shell
cookiecutter gh:{{cookiecutter.github_username}}/cookiecutter-datascience
```

### git

Version control goes without saying. For the local repository,

```shell
git init
git add .
git commit -m "First commit"
```

For the remote repository, make a github repository named `{{cookiecutter.project_name}}`,

```shell
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git
git remote -v
git push origin main
```

and that's it for git.

#### One-liners

We can summarize the above procedure in two one-liners, should you care about doing this fast.

```shell
git init; git add .; git commit -m "First commit";
```

and

```shell
git remote add origin git@github.com:{{cookiecutter.github_username}}/{{cookiecutter.project_name}}.git; git remote -v; git push origin main
```

### Conda Environments

#### Introduction

For **local dependency managment** (LDM), we rely on [conda](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf).

This is completely independent from **remote dependency managment** (RDM). RDM is managing the dependencies on a user's machine, a user who is trying to run your code. For instance, in a python project, you release your piece of code (a "package" in python lingo) through [PyPi](https://pypi.org/). In that _pypi-release_, you need to specify what you expect to find on a user's machine to make your code run.

In conclusion, LDM and RDM are managed independently, because mixing them adds complexity instead of removing it. This has one important downside: **they need to be kept mutually consistent, manually**. This is the price we pay for isolation.

#### Conda Workflow

To create our default environment,

```shell
conda env create -f dependencies.yaml -n {{cookiecutter.project_name}}
```

to additionally add the packages which are relevant for the development phase, do

```shell
conda activate {{cookiecutter.project_name}}
conda env update -n {{cookiecutter.project_name}} -f dependencies-develop.yaml
```

Some dependencies are relevant during development, but not for deployment. For instance any tool that generates documentation websites (e.g. `mkdocs`) is useful for development, but has nothing to do with the actual functionality of your code. As such, we need two `yaml` files, to make that distinction. 

Note that this particular distinction is still different from the distinction between LDM and RDM made above. Essentially, RDM is about ensuring that a user that downloads your code has the same dependencies as specified in your deployment environment.

#### Expose Conda to Jupyterlab

To add your isolated python installation (i.e., the one in your new conda environment) to the list of *"kernels"* found by Jupyter, execute the following.

```shell
conda activate {{cookiecutter.project_name}}
python -m ipykernel install --user --name {{cookiecutter.project_name}}
```


### Local Installation

One fundamental assumption is the following; 

> All code in this repository belongs to one of the two following categories: **source code** or **executable scripts**.

- Code in [src](./src) is considered source code. It composes a Python package.
- Code in [note](./note) are standalone scripts (in notebook form, but these are scripts at heart).

This means that even our own code has to be installed before we are able to use it. This is a pedantic way of doing things, but has some important advantages as well:

1. Scripts see our own algorithm(s) and external competitors both as packages to be imported. This equal footing enforces code quality (e.g., modularity, API-design, ...) and reproducibility.
2. Structuring our code immediately as a package on our local machine, makes the transition to an actual publishable package a lot smoother. In this way, we try to get it right from the start.

#### Python Package Local Install

To install, activate the conda environment and execute this line of code.

```shell
pip install -e . 
```

Every time you change something in your codebase, the installed package in your python environment will also change. Typically, this is what you want: to see your changes reflected immediately during development.


## Distribution workflows

This part is about publishing your project on PyPi.

### PyPi

Make your project publicly available on the Python Package Index, [PyPi](https://pypi.org/). To achieve this, we need **remote dependency managment**, since you want your software to run without forcing users to recreate your conda environments. All dependencies have to be managed, automatically, during installation. To make this work, we need to do some extra work.

We follow the steps as outlined in the most basic (and official) [PyPi tutorial](https://packaging.python.org/tutorials/packaging-projects/).

#### Generate distribution archives

Generate distribution packages for the package. These are archives that are uploaded to the Package Index and can be installed by pip.

```shell
python setup.py sdist bdist_wheel
```

After this, your package can be uploaded to the python package index. To see if it works on PyPi test server, do

```shell
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```

and this will prompt some questions, but your package will end up in the index.

To make your package end up in the actual PyPi, the procedure is almost as simple, do


```shell
python -m twine upload --repository-url https://pypi.org/legacy/ dist/*
```

### Docs

Every good open source project has at least a bit of documentation. A part of this documentation is generated from decent docstrings you wrote together with your code.

#### MKdocs Introduction 

We use [Mkdocs](https://www.mkdocs.org/), with its [material](https://squidfunk.github.io/mkdocs-material/) theme. This generates very nice webpages and feels a bit more modern than Sphinx (which is also great!).

The main upside of `mkdocs` is the fact that its source files are [markdown](https://en.wikipedia.org/wiki/Markdown), the most basic formatted text format there is. For instance, github readmes (including the one you are reading now) are also written in markdown. In that sense, we get consistency, all the stuff that we want to communicate is written in markdown: 

- readme's in the repo
- text cells in jupyter notebooks
- source files for the documentation site

This means that we can write everything once, and link it together. All the formats are the same, hence trivially compatible.

#### Basic MKdocs Commands

This cookiecutter already contains the [mkdocs.yml](mkdocs.yml) file, which is -unsurprisingly- the configuration file for your mkdocs project. Using this cookiecutter, you can focus on content. Alongside this configuration file, we also included a demo page; [index.md](./docs/index.md), which is the home page of the documentation website. 

For a test drive, you need to know some commands. To build your website (i.e., generate html starting from your markdown sources), you do

```shell
mkdocs build
```

To preview your website locally, you do

```shell
mkdocs serve
```

and surf to [localhost:8000](http://localhost:8000). Note that this server does automatic rebuilds, so any changes on disk are reflected immediately.

One-liner for the lazy,

```shell
mkdocs build;mkdocs serve
```

#### Convert Tutorial Notebooks to Docs

Notebooks in `note/tutorial` can be auto-exported to a markdown document and added in the `docs` folder,

```shell
jupyter nbconvert note/tutorial/*.ipynb --to markdown --output-dir=docs
```

#### Hosting Docs on Github

Now, the last challenge is to make this website available over the internet. Luckily, mkdocs makes this [extremely easy](https://www.mkdocs.org/user-guide/deploying-your-docs/) when you want to host on [github pages](https://pages.github.com/)

```bash
mkdocs gh-deploy
```

and your site should be online at; [https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_name}}/](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_name}}/). 

What happens under the hood is that a `mkdocs build` is executed, followed by pushing the `site` directory to the `gh pages` branch in your repository. Github takes care of the rest.


### Repository Description

Often overlooked, but this is right on top of your repository and hence the absolute perfect place to link to your project website. Hence, a cookiecutter-generated sentence to put there would be;

> {{cookiecutter.short_description}}, cf. https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_name}}

N.B. You need to do this manually!


### Docker

Reproducible containers in their most popular form. WIP.

