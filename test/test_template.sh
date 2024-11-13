#!/bin/bash

# This is a collection of commands that will be run only during the test phase.

set -u
set -e

deactivate || true

# activate 
if [[ -d .venv ]]; then
    source .venv/bin/activate
else
    echo "No virtualenv found."
    python -m venv .venv
    source .venv/bin/activate
fi

make setup
make install_dev

git init &&
    git add README.md &&
    git commit -m "first commit"

dvc repro
deactivate