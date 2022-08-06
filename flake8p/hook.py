"""Hooks TOML parser into Flake8."""

import flake8.main.cli
import flake8.options.config
import sys
if sys.version_info >= (3, 11):
    import tomllib as toml
else:
    import tomli as toml
from pathlib import Path


# Remember original Flake8 objects.
flake8_RawConfigParser  = flake8.options.config.configparser.RawConfigParser
flake8_find_config_file = flake8.options.config._find_config_file


# Implement derived objects that are aware of `pyproject.toml`.

class RawConfigParser(flake8_RawConfigParser):
    """Mixes the TOML parser into Flake8's config-file parser."""

    def _read(self, stream, path):
        file = Path(path)
        if file.name == 'pyproject.toml':
            with file.open('rb') as f:
                settings = toml.load(f)
            if not self.has_section('flake8'):
                self.add_section('flake8')
            for (key, value) in settings['tool']['flake8'].items():
                if isinstance(value, (bool, int, float)):
                    value = str(value)
                self.set('flake8', key, value)
        else:
            super()._read(stream, path)


def find_config_file(path):
    """Convinces Flake8 to prefer `pyproject.toml` over other config files."""
    file = Path(path)/'pyproject.toml'
    if file.exists():
        with file.open('rb') as f:
            settings = toml.load(f)
        if 'tool' in settings and 'flake8' in settings['tool']:
            return str(file)
    return flake8_find_config_file(path)


# Monkey-patch Flake8 with our modified objects.
flake8.options.config.configparser.RawConfigParser = RawConfigParser
flake8.options.config._find_config_file = find_config_file

# Just call Flake8 when we are called.
main = flake8.main.cli.main
