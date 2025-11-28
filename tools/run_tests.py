"""Runs the test suite."""

from subprocess import run
from pathlib    import Path


root = Path(__file__).resolve().parent.parent

run(['pytest'], cwd=root)
