## Developer tools

These are simple helper scripts to run the various dev tools, such as the test
suite or to build the distribution wheel. See the doc-strings of the individual
scripts for details.

For local development, install the package in editable mode inside a dedicated
virtual environment with `pip install --editable .[dev]`.


### Releasing a new version

- Bump version number in `meta.py`.
- Add dedicated commit for the version bump.
- Publish to PyPI via GitHub Action.
- Create release on GitHub, tag it (like `v1.2.4`), add release notes.
