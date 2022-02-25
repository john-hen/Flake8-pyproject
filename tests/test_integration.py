"""Integration tests for the package."""

from subprocess import run, PIPE
from pathlib import Path
from sys import executable as python


expected = r"""
module.py:1:71: E501 line too long (77 > 70 characters)
module.py:5:14: E221 multiple spaces before operator
2
""".strip()


def capture(command, fixture):
    folder  = Path(__file__).parent/'fixtures'/fixture
    process = run(command, stdout=PIPE, text=True, cwd=folder)
    return process.stdout.strip()


def test_config_pyproject():
    output = capture(['flake8p', 'module.py'], 'config_pyproject')
    assert output == expected


def test_config_flake8():
    output = capture(['flake8p', 'module.py'], 'config_flake8')
    assert output == expected


def test_config_setup():
    output = capture(['flake8p', 'module.py'], 'config_setup')
    assert output == expected


def test_config_tox():
    output = capture(['flake8p', 'module.py'], 'config_tox')
    assert output == expected


def test_config_mixed():
    output = capture(['flake8p', 'module.py'], 'config_mixed')
    assert output == expected


def test_run_main():
    output = capture([python, '-m', 'flake8p', 'module.py'], 'config_mixed')
    assert output == expected


def test_empty_folder():
    output = capture(['flake8p'], 'empty_folder')
    assert not output


def test_empty_pyproject():
    output = capture(['flake8p'], 'empty_pyproject')
    assert not output


def test_empty_tool_section():
    output = capture(['flake8p'], 'empty_tool_section')
    assert not output
