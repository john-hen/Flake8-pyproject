"""Calls main entry point if run via `python -m flake8p`."""

from . import main

if __name__ == '__main__':
    raise SystemExit(main())
