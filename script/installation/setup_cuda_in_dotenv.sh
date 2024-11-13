#!/bin/bash

set -e
# set -u

CONDA_PREFIX=/opt/miniconda3
CUDNN_PATH=$(dirname $(python -c "import nvidia.cudnn;print(nvidia.cudnn.__file__)"))
LD_LIBRARY_PATH=$CONDA_PREFIX/lib/:$CUDNN_PATH/lib:/opt/miniconda3/lib/:$LD_LIBRARY_PATH

cat - << EOF >> .env
# inserted by script/installation/setup_cuda_in_dotenv.sh
# this would enable poetry to use conda
CONDA_PREFIX=${CONDA_PREFIX}
CUDNN_PATH=${CUDNN_PATH}
LD_LIBRARY_PATH=${LD_LIBRARY_PATH}
EOF
