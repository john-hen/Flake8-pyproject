"""Integration tests for the package."""

from pathlib import Path
from subprocess import PIPE, run
from sys import executable as python

from pytest import mark

expected = r"""
module.py:1:71: E501 line too long (77 > 70 characters)
module.py:5:14: E221 multiple spaces before operator
2
""".strip()


def capture(command, folder):
    if isinstance(folder, str):
        folder = Path(__file__).parent/'fixtures'/folder
    process = run(command, stdout=PIPE, universal_newlines=True, cwd=folder)
    # From Python 3.7 on, use `text=True` instead of `universal newlines`.
    return process.stdout.strip()


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_config_pyproject(command):
    output = capture([command, 'module.py'], 'config_pyproject')
    assert output == expected


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_config_flake8(command):
    output = capture([command, 'module.py'], 'config_flake8')
    assert output == expected


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_config_setup(command):
    output = capture([command, 'module.py'], 'config_setup')
    assert output == expected


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_config_tox(command):
    output = capture([command, 'module.py'], 'config_tox')
    assert output == expected


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_config_mixed(command):
    output = capture([command, 'module.py'], 'config_mixed')
    assert output == expected


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_config_toml(command):
    here = Path(__file__).parent
    file = here/'fixtures'/'config_toml'/'flake8.toml'
    output = capture([command, f'--toml-config={file.name}', 'module.py'],
                     'config_toml')
    assert output == expected
    output = capture([command, f'--toml-config={file.resolve()}', 'module.py'],
                     'config_toml')
    assert output == expected


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_empty_folder(command):
    output = capture([command], 'empty_folder')
    assert not output


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_empty_pyproject(command):
    output = capture([command], 'empty_pyproject')
    assert not output


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_empty_tool_section(command):
    output = capture([command], 'empty_tool_section')
    assert not output


@mark.parametrize('command', ['flake8', 'flake8p'])
def test_run_main(command):
    output = capture([python, '-m', command, 'module.py'], 'config_mixed')
    assert output == expected
