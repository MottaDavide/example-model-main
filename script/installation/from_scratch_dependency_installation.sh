#!/bin/bash

pdm add \
    "polars" \
    "typer" \
    "pydantic[dotenv]" \
    "scikit-learn" \
    "pyarrow" \
    "pydantic-settings" \
    "mkdocs-minify-plugin" \
    "matplotlib" \
    "ipywidgets" \
    "plotly"

pdm add -dG \
    "dvc" \
    "dvclive" \
    "pytest"

pdm add --group doc \
    "mkdocs" \
    "mkdocs-material" \
    "mkdocs-macros-plugin" \
    "mkdocstrings" \
    "mkdocs-autorefs" \
    "mkdocs-simple-plugin" \
    "mkdocs-jupyter" \
    "mkdocs-redirects" \
    "mkdocs-gallery" \
    "mkdocstrings-crystal"
