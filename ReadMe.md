# Flake8-pyproject / flake8p
*Runs Flake8 with configuration from `pyproject.toml`*

[Flake8] cannot be configured via `pyproject.toml`, even though
virtually all other Python dev tools have adopted it as the central
location for project configuration. The discussion of the original
proposal ([#234]) was closed as "too heated", subsequent feature
and pull requests were marked as "spam" ([#1332], [#1421], [#1431],
[#1447], [#1501]).

**Flake8-pyproject** also has bad manners and force-feeds Flake8 the
spam it so despises. It is inspired by [pyproject-Flake8], which had
received little maintenance following its initial commit. The code was
however completely rewritten and a simple test suite makes it all a
little more palatable.

[Flake8]:           https://github.com/PyCQA/flake8
[#234]:             https://github.com/PyCQA/flake8/issues/234
[#1332]:            https://github.com/PyCQA/flake8/pull/1332
[#1421]:            https://github.com/PyCQA/flake8/issues/1421
[#1431]:            https://github.com/PyCQA/flake8/issues/1431
[#1447]:            https://github.com/PyCQA/flake8/issues/1447
[#1501]:            https://github.com/PyCQA/flake8/issues/1501
[pyproject-flake8]: https://github.com/csachs/pyproject-flake8


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

From then on run `flake8p` instead of `flake8` to lint the code so
 that the configuration in `pyproject.toml` will be used.

[TOML format]: https://toml.io


## Implementation

Flake8 uses [`RawConfigParser`] from the standard library to parse its
configuration files, and therefore expects them to have the [INI format].

This library adds `pyproject.toml` to Flake8's list of acceptable
configuration files and monkey-patches Flake8's `RawConfigParser` class
definition so that, when `pyproject.toml` is being read, the format is
converted from TOML to INI on the fly. TOML parsing is handled by
[Tomli], which will be part of the standard library as of Python 3.11
([PEP 680]).

A few very simple integration tests round out the package, making sure
that any one of the possible configuration files are in fact accepted.

[`RawConfigParser`]: https://docs.python.org/3/library/configparser.html#configparser.RawConfigParser
[INI format]:        https://en.wikipedia.org/wiki/INI_file#Format
[Tomli]:             https://pypi.org/project/tomli/
[PEP 680]:           https://www.python.org/dev/peps/pep-0680


[![release](
    https://img.shields.io/pypi/v/Flake8-pyproject.svg?label=release)](
    https://pypi.python.org/pypi/Flake8-pyproject)
[![coverage](
    https://img.shields.io/codecov/c/github/john-hen/Flake8-pyproject?token=lU8tHs0Bpe)](
    https://codecov.io/gh/john-hen/Flake8-pyproject)
[![quality](
    https://img.shields.io/lgtm/grade/python/github/john-hen/Flake8-pyproject?label=quality)](
    https://lgtm.com/projects/g/john-hen/Flake8-pyproject)
