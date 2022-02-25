"""Hooks TOML parser into Flake8."""

import tomli
from pathlib import Path
from flake8.main.cli import main as flake8_main
from flake8.options import config as flake8_config


class PyprojectRawConfigParser(flake8_config.configparser.RawConfigParser):
    """Mixes the TOML parser into Flake8's INI parser."""

    def _read(self, stream, path):
        file = Path(path)
        if file.name == 'pyproject.toml':
            with file.open('rb') as f:
                settings = tomli.load(f)
            if 'tool' not in settings:
                return
            if 'flake8' not in settings['tool']:
                return
            if not self.has_section('flake8'):
                self.add_section('flake8')
            for (key, value) in settings['tool']['flake8'].items():
                if isinstance(value, (bool, int, float)):
                    value = str(value)
                self.set('flake8', key, value)
        else:
            super()._read(stream, path)


class PyprojectConfigFileFinder(flake8_config.ConfigFileFinder):
    """Adds `pyproject.toml` to the list of accepted configuration files."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.project_filenames = self.project_filenames + ('pyproject.toml',)


flake8_config.configparser.RawConfigParser = PyprojectRawConfigParser
flake8_config.ConfigFileFinder             = PyprojectConfigFileFinder

main = flake8_main
