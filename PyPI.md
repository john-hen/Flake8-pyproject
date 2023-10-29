# Flake8-pyproject
*Flake8 plug-in loading the configuration from `pyproject.toml`*

[Flake8] cannot currently be configured via `pyproject.toml`, the file
which has been [proposed by PEP-518 for tool configuration][pep518]
and which has been adopted by many other Python code quality tools.
Though the project has tentative plans to support `pyproject.toml`, it
has been [considered blocked][blocked] on other tools' behavior for
years.

This means that developers wishing to consolidate their configuration
files are still unable to fully do so. Enter Flake8-pyproject, which
registers itself as a Flake8 plug-in and allows seamlessly loading the
tool's configuration from `pyproject.toml` when you run the `flake8`
command.

[Flake8]:  https://github.com/PyCQA/flake8
[pep518]:  https://peps.python.org/pep-0518/#tool-table
[blocked]: https://github.com/PyCQA/flake8/issues/234#issuecomment-812800722


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
