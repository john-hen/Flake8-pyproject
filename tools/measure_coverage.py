"""Measures code coverage by test suite."""

from subprocess import run
from pathlib import Path
from sys import executable as python

here = Path(__file__).resolve().parent
root = here.parent

print('Running test suite.')
run(
    [
        python, '-m', 'pytest',
        '--cov',
        '--cov-report=html',
        '--cov-report=xml',
        '--cov-report=term'
    ],
    cwd=root,
)
