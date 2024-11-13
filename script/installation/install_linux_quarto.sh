#!/bin/bash

QUARTO_VERSION="1.2.262"

mkdir -p .opt/quarto/${QUARTO_VERSION}

curl -o quarto.tar.gz -L \
    "https://github.com/quarto-dev/quarto-cli/releases/download/v${QUARTO_VERSION}/quarto-${QUARTO_VERSION}-linux-amd64.tar.gz"

tar -zxvf quarto.tar.gz \
    -C ".opt/quarto/${QUARTO_VERSION}" \
    --strip-components=1

rm quarto.tar.gz

export PATH="$PATH:$PWD/.opt/quarto/${QUARTO_VERSION}/bin"

echo -e "Quarto installed successfully. Quarto version: ${QUARTO_VERSION}"

echo -e "Getting started at:\n\thttps://quarto.org/docs/get-started/hello/vscode.html"

echo -e "Render a document with:\n\tquarto render <document>"

# Test quarto
quarto check

exit $?
