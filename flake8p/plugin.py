from typing import List

from .util import monkeypatch

class FlakeConfigToml:
    # pylint: disable=no-self-use
    """
    Flake8 plugin to load a `pyproject.toml` file from the current directory.
    """
    # Pylint warning disabled because this is a plugin and these methods
    # need to be present...but we don't need to use `self`.
    def __init__(self, tree):
        pass

    def __iter__(self):
        raise StopIteration()

    def run(self, *args) -> List[Any]:
        return []

    def add_options(self, *args):
        monkeypatch()
