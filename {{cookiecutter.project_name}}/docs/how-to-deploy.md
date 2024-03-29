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

#### Notebooks, `git` and `merge conflict` hell

Pro-tip: notebooks and git do not work well together, because notebooks mix code, outputs and comments all together. 
That's what makes them great, but has a side-effect of making them absolutely horrible with git.
For instance, notebooks even keep track of how many times a single cell has been executed! 
That means that a notebook with identical code, comments and outputs can still cause some change to be tracked by git, despite the fact that absolutely nothing of any relevance changed.
What makes this particularly bad is that
- a) outputs can differ _wildly_ with only small (relevant) changes in code and
- b) those outputs are being saved in the same file as the code itself and 
- c) this causes _all_ the content (including code!) to shift from line to line, causing enormous diffs. This is because `git` basically works on the idea that line numbers mean something.

Basically, this leads to two huge issues
1. This makes it impossible for humans to follow what's going on wrt to changes being made. After all, `.ipynb` files are not designed to be human-readable, but are meant to be rendered in browser.
2. In practice, this leads to _"merge-conflict-hell"_: typically, to solve merge conflicts, you dig into your code and see where the irreconcible diffs are. But, due to the former issue, this becomes a titanic (and pointless!) task when notebooks are involved.
    
TL;DR: keep your notebook outputs out of `git`, **always**. 

How you accomplish the above is up to you, personally I have found the tool [nbstripout](https://github.com/kynan/nbstripout) to do the trick. 
Just `cd` into the directory where you are working in, make sure you are on the correct branch in `git` and run this command;
    
```shell
nbstripout --install
```    
and changes in your notebooks should not lead to content in your commits anymore.
[Git hooks](https://www.atlassian.com/git/tutorials/git-hooks) would also be an option, but I never got those to work reliably. YMMV though.

### Conda Environments

#### Introduction

For **local dependency managment** (LDM), we rely on [conda](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf). This is completely independent from **remote dependency managment** (RDM). 

- RDM is managing the dependencies on _the user's_ machine, e.g. a user who is trying to run your code. For instance, in a python project, you release your piece of code (a "package" in python lingo) through [PyPi](https://pypi.org/). In that _pypi-release_, you need to specify what you expect to find on a user's machine to make your code run. 
- LDM is about making the code run on _our_ machines. This matters for several reasons. First, you yourself may occasionally switch machines (e.g. laptop/desktop or home/office, etc). Second, team members working on the same codebase typically do not share one single machine on which they do so. Hence, team members also need their respective machines to be configured similarly. This is the programmer equivalent of the hollywood trope "synchronize watches".

In conclusion, LDM and RDM are different and therefore managed independently: mixing them adds complexity instead of removing it. This has one important downside: **they need to be kept mutually consistent, manually**. This is the price we pay for isolation.

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

To install, activate the conda environment (`conda activate {{cookiecutter.project_name}}`) and execute this line of code.

```shell
pip install -e . 
```

Every time you change something in your codebase, the installed package in your python environment will change automatically. Typically, this is what you want: to see your changes reflected immediately during development.


## Distribution workflows

This part is about publishing your project on [PyPi](https://pypi.org/).

### PyPi

Make your project publicly available on the _Python Package Index_, [PyPi](https://pypi.org/). To achieve this, we need **remote dependency managment**, since you want your software to run without forcing users to recreate your conda environments. All dependencies have to be managed, automatically, during installation. To make this work, we need to do some extra work.

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

Every good project has at least a bit of documentation. Part of this documentation is generated from decent docstrings you wrote together with your code. Writing functions without docstrings is a lot like playing russian roulette: at some point, you will regret the decision.

#### MkDocs Introduction 

We use [MkDocs](https://www.mkdocs.org/), with its [material](https://squidfunk.github.io/mkdocs-material/) theme. This generates very nice webpages and feels a bit more modern than [Sphinx](https://www.sphinx-doc.org/en/master/) (which is also great!).

The main upside of `mkdocs` is the fact that its source files are [markdown](https://en.wikipedia.org/wiki/Markdown), the most basic text format there is. For instance, github readmes (including the one you are reading now) are also written in markdown. This yields _consistency_: all the stuff that we want to communicate is written in markdown: 

- readme's in the repo
- text cells in jupyter notebooks
- source files for the documentation site

This means that we need to write everything once, and add it to docs if we want it to be there. All the formats are the same, hence trivially compatible.

#### Basic MkDocs Commands

This cookiecutter already contains the [mkdocs.yml](mkdocs.yml) file, which is -unsurprisingly- the configuration file for your mkdocs project. Using this cookiecutter, you can focus on content. Alongside this configuration file, we also included a demo page; [index.md](./docs/index.md), which will be the home page of the documentation website. 

For a test drive, you need to know some commands. To build your website (generate html starting from your markdown sources), you do

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

```shell
mkdocs gh-deploy
```

and your site should be online at; [https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_name}}/](https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_name}}/). 

What happens under the hood is that a `mkdocs build` is executed, followed by pushing the `site` directory to the `gh pages` branch in your repository. Github takes care of the rest.


### Repository Description

Often overlooked, but this is right on top of your repository and hence the absolute perfect place to link to your project website. Hence, a cookiecutter-generated sentence to put there would be;

> {{cookiecutter.short_description}}, cf. https://{{cookiecutter.github_username}}.github.io/{{cookiecutter.project_name}}

N.B. This cannot be automated, you must do this manually. In fact, if you are reading this: do it **now**.


### Docker

Reproducible containers in their most popular form. WIP.

