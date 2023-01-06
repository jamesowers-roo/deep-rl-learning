# Install

```shell
conda create --name deep-rl-learning python=3.10 --channel conda-forge --yes
conda activate deep-rl-learning
conda install pytorch torchvision torchaudio --channel pytorch --yes
# needed for Apple Silicon M1/M2/M3 Macs for pytorch lightning
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
poetry install
pre-commit install --install-hooks
```