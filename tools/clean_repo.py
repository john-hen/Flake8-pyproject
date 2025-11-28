"""Deletes build and test artifacts."""

from pathlib import Path
from shutil import rmtree


root = Path(__file__).resolve().parent.parent

folders = [
    root/'build',
    root/'dist',
]
folder_names = [
    '__pycache__',
    '.pytest_cache',
]

for folder_name in folder_names:
    for folder in root.rglob(folder_name):
        folders.append(folder)

for folder in folders:
    if folder.is_dir():
        rmtree(folder, ignore_errors=True)
