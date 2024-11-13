#!/bin/bash

rm -rf data/dvc/07_build/
mkdir -p data/dvc/07_build/

# build package
pdm build
mv dist/*.whl data/dvc/07_build/

# wrap the model
cp data/dvc/03_train/model_fit.pkl data/dvc/07_build/

# wrap the other materials
cp script/build_material/* data/dvc/07_build/
