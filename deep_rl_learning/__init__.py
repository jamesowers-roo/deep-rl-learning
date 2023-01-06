from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("merchandising_algos_models")
except PackageNotFoundError:
    pass
