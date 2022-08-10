"""Hooks TOML parser into Flake8."""

from . import util

import flake8.main.cli
import flake8.options.config
from pathlib import Path
from typing import Any, List


# Remember original Flake8 objects.
flake8_RawConfigParser  = flake8.options.config.configparser.RawConfigParser
flake8_find_config_file = flake8.options.config._find_config_file


# Implement derived objects that are aware of `pyproject.toml`.

class RawConfigParser(flake8_RawConfigParser):
    """Mixes the TOML parser into Flake8's config-file parser."""

    def _read(self, stream, path):
        file = Path(path)
        if file.name == 'pyproject.toml':
            settings = util.load_flake8_from_toml(file)
            if not self.has_section('flake8'):
                self.add_section('flake8')
            settings = util.normalize_from_toml(settings)
            for (key, value) in settings['flake8'].items():
                self.set('flake8', key, value)
        else:
            super()._read(stream, path)


def find_config_file(path):
    """Convinces Flake8 to prefer `pyproject.toml` over other config files."""
    config_path, config = util.find_and_load_toml_file(path)
    if config_path is not None and "flake8" in config:
        return str(config_path)
    return flake8_find_config_file(path)

# Monkey-patch Flake8 with our modified objects.
flake8.options.config.configparser.RawConfigParser = RawConfigParser
flake8.options.config._find_config_file = find_config_file

# Just call Flake8 when we are called.
main = flake8.main.cli.main


class Plugin:
    """Installs the hook when called via `flake8` itself."""

    def add_options(self, *args):
        util.monkeypatch()
