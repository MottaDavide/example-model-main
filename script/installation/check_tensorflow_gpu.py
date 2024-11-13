# %%
import tensorflow as tf
from tensorflow.python.platform import build_info as tf_build_info
import subprocess

# %%
if tf.test.is_built_with_cuda():
    print("Tensorflow was built with CUDA")
    print(f"cuda_version: {tf_build_info.build_info['cuda_version']}")
    print(f"cudnn_version: {tf_build_info.build_info['cudnn_version']}")
else:
    print("tensorflow was NOT build with CUDA")
    subprocess.run(["nvcc", "--version"])

print(tf_build_info.build_info)
print("list of physical GPUs: ", tf.config.list_physical_devices("GPU"))

# %%
