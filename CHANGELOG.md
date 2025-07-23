# CHANGELOG

## Unreleased changes

* Support Python 3.12 and 3.13.
* Drop support for EOL Python versions.
* Fix a typo in the `--toml-config` option metavar.

## v1.2.3 -- 2023-03-21

* Fix: Don't error when parsing unknown command-line arguments.
* Fix: Don't assume `sys.argv` only contains Flake8's command-line options.

## v1.2.2 -- 2022-12-04

* Recommend using the Flake8 pre-commit hook directly.
* Remove upper-bound pin for Flake8.
* Clarify the pre-commit config documentation.

## v1.2.1 -- 2022-11-25

* Support Flake8 v6.x.

## v1.2.0 -- 2022-11-17

* Update project front page / documentation.
* Update project metadata and dev config.
* Add command-line option for custom config file.

## v1.1.0.post0 -- 2022-08-13

* Update short description in PyPI metadata.
* Fix: Resolve typos in ReadMe and PyPI summary.

## v1.1.0 -- 2022-08-11

* Update documentation to explain plug-in mechanism.
* Remove old hook. Rely on the plug-in hook from now on.
* Change plug-in type from "extension" to "report".
* Move plug-in implementation to `hook.py`.

## v1.0.1 -- 2022-08-06

* No longer require TOMLi as of Python 3.11.
* Fix: Ensure `python -m flake8p` returns an exit code.

## v1.0.0 -- 2022-08-01

* Update documentation.
* Support Flake8 v5.x and drop support for earlier versions.

## v0.9.1 -- 2022-08-01

* Support Python 3.6
* Require Flake8 versions earlier than 5.
* Document using pre-commit.

## v0.9.0 -- 2022-02-25

* Initial release.
