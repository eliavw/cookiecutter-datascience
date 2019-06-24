# Deployment Information

We use git for versioning and conda for package managment.

## Github init

Create an empty repository on github, then;

```bash
git init
git add .
git commit -m "First commit"
git remote add origin git remote add origin git@github.com:eliavw/{{project_name}}.git
git remote -v
git push origin master
```

## Create

Environment made with conda. To make an environment;

```bash
conda create --name {{cookiecutter.project_name}} python=3.7
```

## Export
This environment can be exported to a `.yml` file through the following command:

```bash
conda env export > environment.yml
```

Which creates the `.yml` file present in the root dir.


## Load
To recreate this environment, it suffices to run;

```bash
conda env create -f environment.yml -n {{cookiecutter.project_name}} 
```

Which presupposes a miniconda on your own machine.

## Add kernel to Jupyter

To add this python environment to the list of Jupyter environments, do the following. 
```bash
source activate {{cookiecutter.project_name}}
python -m ipykernel install --user --name {{cookiecutter.project_name}} --display-name "{{cookiecutter.project_name}}"
```

_N.b.: This requires ipykernel to be installed in the environment._
