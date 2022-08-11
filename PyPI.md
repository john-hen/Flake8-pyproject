# Flake8-pyproject
*Flake8 plug-in loading the configuration from `pyproject.toml`*

[Flake8] cannot be configured via `pyproject.toml`, even though
virtually all other Python dev tools have adopted it as the central
location for project configuration. The discussion of the original
proposal ([#234]) was closed as "too heated", subsequent feature
and pull requests were marked as "spam" ([#1332], [#1421], [#1431],
[#1447], [#1501]).

*Flake8-pyproject* also has bad manners and force-feeds Flake8 the
spam it so despises.

It is inspired by [pyproject-Flake8], though the code was rewritten
from scratch, a test suite was added to make maintenance easier, and
a Flake8 plug-in makes this work with the regular `flake8` command.

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

Then run `flake8` in the project root folder, where `pyproject.toml`
is located.

For compatibility with earlier versions of this package, and perhaps
extra reliability in terms of possible future breakage of the plug-in
hook, the package also provides a `flake8p` command that could be
called alternatively to lint the code.

[TOML format]: https://toml.io
