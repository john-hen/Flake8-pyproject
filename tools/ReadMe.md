## Developer tools

These are simple helper scripts to run the various dev tools, such as
pyTest or Flit. See the doc-strings of the individual scripts for
details.

For local development, install the package in editable mode inside a
dedicated virtual environment: `pip install --editable .[dev]`.


### Releasing a new version

* Bump version number in `meta.py`.
* Add dedicated commit for the version bump.
* Tag commit with version number, e.g. `git tag 1.0.0`.
* Push to GitHub: `git push && git push --tags`.
* Create GitHub release from tag and add release notes.
* Publish to PyPI: `tools/publish.py`.
