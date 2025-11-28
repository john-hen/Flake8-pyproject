"""Measures code coverage by test suite."""

from subprocess import run
from pathlib    import Path
from sys        import executable as python


print('Running test suite.')
root = Path(__file__).resolve().parent.parent
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
