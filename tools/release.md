Steps to take when releasing a new version:
* Bump version number in `meta.py`.
* Add dedicated commit for the version bump.
* Push to GitHub: `git push origin main`.
* Tag commit with version number, e.g. `git tag 0.9.0`.
* Push the new tag: `git push --tags`.
* Run code coverage and upload report to CodeCov.
* Create new release on GitHub and add release notes.
* Publish to PyPI by running `deploy/publish.py`.
