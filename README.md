# cookiecutter-datascience

Cookiecutter template for datascience

## Workflow

### Creation

Using the power of both `PyScaffold` and `cookiecutter` templates, this single command provides a pretty solid starting point for any new project.

```bash
putup project-name --cookiecutter gh:eliavw/cookiecutter-datascience --markdown
```

### Github

Create an empty repository on github, then;

```bash
git init
git add .
git commit -m "First commit"
git remote add origin <remote repository URL>
git remote -v
git push origin master
```

## Todo

- CI workflow
- Doc workflow
- Reproducibility 01 workflow (tracking packages)
- Reproducibility 02 singularity or Docker workflow 
