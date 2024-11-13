# DVC

## Introduction

Dvc is the tool to version data and models. It relies on Git.

Here some commands:

```sh
dvc repro
dvc params diff 
dvc metrics diff
dvc dag
dvc exp run
dvc exp show
dvc exp branch <exp> <branch>
dvc exp apply <exp>
```

Code examples: https://code.dvc.org/get-started/code.zip

## Configuration

Config files locations:

- `.dvc/`

## Store big datasets

### Setup a remote

follow this [guide](https://dvc.org/doc/user-guide/how-to/setup-google-drive-remote#how-to-setup-a-google-drive-dvc-remote)

See also: https://dvc.org/doc/start/data-management/data-versioning#storing-and-sharing

```sh
dvc remote add --default vl_gdrive gdrive://1rV2edmwEmD6ecgUlXivPw2m9u4ggfwvv
```

### add a file or folder

```sh
dvc add data/persistent/file.csv
```

This creates a file.csv.dvc file and git-ignores the original.



## Develop

### Templates

```sh
dvc plots templates simple > .dvc/plot_template/bars_template.json
dvc plots show data.csv --template .dvc/plot_template/bars_template.json
```
