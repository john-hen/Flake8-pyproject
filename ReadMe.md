# Flake8-pyproject
*Flake8 plug-in loading the configuration from `pyproject.toml`*

[Flake8] cannot be configured via `pyproject.toml`, even though
virtually all other Python dev tools have adopted it as the central
location for project configuration. The discussion of the original
proposal ([#234]) was closed as "too heated", subsequent feature
and pull requests were marked as "spam" ([#1332], [#1421], [#1431],
[#1447], [#1501]).

Flake8-pyproject also has bad manners and force-feeds Flake8 the
spam it so despises. It registers itself as a Flake8 plug-in to
seamlessly load the configuration from `pyproject.toml` when you
run the `flake8` command.

[Flake8]: https://github.com/PyCQA/flake8
[#234]:   https://github.com/PyCQA/flake8/issues/234
[#1332]:  https://github.com/PyCQA/flake8/pull/1332
[#1421]:  https://github.com/PyCQA/flake8/issues/1421
[#1431]:  https://github.com/PyCQA/flake8/issues/1431
[#1447]:  https://github.com/PyCQA/flake8/issues/1447
[#1501]:  https://github.com/PyCQA/flake8/issues/1501


## Usage

Say your Flake8 configuration in `.flake8` (or in `tox.ini`, or
`setup.cfg`) is this:
```ini
[flake8]
ignore = E231, E241
per-file-ignores =
    __init__.py:F401
max-line-length = 88
count = true
```

Copy that `[flake8]` section to `pyproject.toml`, rename it as
`[tool.flake8]`, and convert the key–value pairs to the [TOML format]:
```toml
[tool.flake8]
ignore = ['E231', 'E241']
per-file-ignores = [
    '__init__.py:F401',
]
max-line-length = 88
count = true
```

Then run `flake8` in the project root folder, where `pyproject.toml`
is located.

In case your TOML-based configuration is contained in a different
folder, or the file has a different name, specify the location with
the `--toml-config` command-line option.

For compatibility with earlier versions of this package, and perhaps
extra reliability in terms of possible future breakage of the plug-in
hook, the package also provides a `flake8p` command that could be
called alternatively to lint the code.

[TOML format]: https://toml.io


## Implementation

Flake8 uses [`RawConfigParser`] from the standard library to parse its
configuration files, and therefore expects them to have the [INI
format].

This library hooks into Flake8's plug-in mechanism to load the
configuration from `pyproject.toml` instead, *if* it finds such a file
in the current folder (working directory). It then creates a
`RawConfigParser` instance, converting from the TOML input format,
and passes it on to Flake8 while discarding configuration options that
would otherwise be sourced from elsewhere.

As of Python 3.11, a TOML parser is part of the standard library ([PEP
680]). On older Python installations, we rely on [Tomli].

A few very simple integration tests round out the package, making sure
that any one of the possible configuration files are in fact accepted
when `pyproject.toml` isn't found.

[`RawConfigParser`]: https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser
[INI format]:        https://en.wikipedia.org/wiki/INI_file#Format
[Tomli]:             https://pypi.org/project/tomli/
[PEP 680]:           https://www.python.org/dev/peps/pep-0680


[![release](
    https://img.shields.io/pypi/v/Flake8-pyproject.svg?label=release)](
    https://pypi.python.org/pypi/Flake8-pyproject)
[![coverage](
    https://img.shields.io/codecov/c/github/john-hen/Flake8-pyproject?token=30Gjak3Ksu)](
    https://codecov.io/gh/john-hen/Flake8-pyproject)
