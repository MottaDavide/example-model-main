# PACKAGE README

<!--

main pipeline: [![pipeline](https://gitlab.com/vanlog/int/lib/temple/badges/main/pipeline.svg)](https://gitlab.com/vanlog/int/lib/temple/-/pipelines)

main coverage: [![coverage](https://gitlab.com/vanlog/int/lib/temple/badges/main/coverage.svg?job=coverage)](https://gitlab.com/vanlog/int/lib/temple/-/pipelines)

-->

description of the package

## Setup

### Setup the project (once, when the repository is cloned)

This setup process is to be done one time, at the moment of cloning the repository.

Procedure:

```bash
# warning: this will change you personal user environment (optional).
make setup
# this will prepare the package environment and install the dependencies
make install_dev
# Initialize a .env file
cp .env_template .env
# edit the env variables
code .env
# load the configuration
source config.sh
```

Activate pre-commit hooks (optional, but advised):

```bash
# Activate the pre-commit configuration of the file .pre-commit-config.yaml
pre-commit install
# get the dvc hooks (once per repository, then it is tracked by git)
dvc install--use-pre-commit-tool
```

### Load the configuration (always)

This is to configure the bash instance with environment variables. *This must be
done for every new bash process.*

```bash
source config.sh
```

