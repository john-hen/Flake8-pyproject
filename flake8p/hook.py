"""Hooks TOML parser into Flake8."""

########################################
# Imports                              #
########################################

from . import meta
import flake8.main.cli
import flake8.options.aggregator
import flake8.options.config
import sys
if sys.version_info >= (3, 11):
    import tomllib as toml
else:
    import tomli as toml
import configparser
from pathlib import Path


########################################
# Hook                                 #
########################################

# Remember original Flake8 objects.
flake8_aggregate_options = flake8.options.aggregator.aggregate_options
flake8_parse_config = flake8.options.config.parse_config

# Global variable pointing to TOML config.
toml_config = Path('pyproject.toml')


def aggregate_options(manager, cfg, cfg_dir, argv):
    """
    Overrides Flake8's option aggregation.

    If a custom TOML file was specified via the `--toml-config`
    command-line option, its value is stored in a global variable for
    later consumption in parse_config().

    Finally, Flake8's `aggregate_options()` is called as usual.
    """
    global toml_config
    arguments = manager.parser.parse_known_args(argv)[0]
    if arguments.toml_config:
        toml_config = Path(arguments.toml_config)
        if not toml_config.exists():
            raise FileNotFoundError(
                f'Plug-in {meta.title} could not find '
                f'custom configuration file "{toml_config}".')
    return flake8_aggregate_options(manager, cfg, cfg_dir, argv)


def parse_config(option_manager, cfg, cfg_dir):
    """
    Overrides Flake8's configuration parsing.

    If we discover `pyproject.toml` in the current folder, we discard
    anything that may have been read from whatever other configuration
    file and read the `tool.flake8` section in `pyproject.toml` instead.

    If a custom TOML file was specified via the `--toml-config`
    command-line option, we read the section from that file instead.
    """
    if toml_config.exists():
        with toml_config.open('rb') as stream:
            pyproject = toml.load(stream)
        if 'tool' in pyproject and 'flake8' in pyproject['tool']:
            parser = configparser.RawConfigParser()
            section = 'flake8'
            parser.add_section(section)
            for (key, value) in pyproject['tool']['flake8'].items():
                if isinstance(value, (bool, int, float)):
                    value = str(value)
                parser.set(section, key, value)
            (cfg, cfg_dir) = (parser, str(toml_config.resolve().parent))

    return flake8_parse_config(option_manager, cfg, cfg_dir)


########################################
# Plug-in                              #
########################################

class Plugin:
    """
    Installs the hook when called via `flake8` itself.

    Also adds the command-line option `--toml-config` to Flake8.
    """
    @classmethod
    def add_options(cls, parser):
        flake8.options.aggregator.aggregate_options = aggregate_options
        flake8.options.config.parse_config = parse_config
        parser.add_option(
            '--toml-config', metavar='TOML_COMFIG',
            default=None, action='store',
            parse_from_config=True,
            help='Path to custom TOML configuration file. May be located in a '
                 'different folder. Overrides the default "pyproject.toml" '
                 'in the current working directory.',
        )


########################################
# Main                                 #
########################################

# Also call Flake8 when we are called via our own `flake8p` entry point.
# We keep this entry point alive for backward compatibility. And also
# in case the plug-in hook breaks, so users have something to fall back
# on that would be easier to fix in our own code. At this point, however,
# we just call Flake8 directly, which will then load the above hook via
# the plug-in mechanism.
main = flake8.main.cli.main
