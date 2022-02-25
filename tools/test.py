"""Runs the test suite."""

from subprocess import run
from pathlib import Path

here = Path(__file__).resolve().parent
root = here.parent
run(['pytest'], cwd=root)
