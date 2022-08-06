from typing import Tuple, Any, Dict, List, Optional
from pathlib import Path
import configparser
import sys

if sys.version_info >= (3, 11):
    import tomllib as toml
else:
    import tomli as toml

import flake8.options.config

def _stat_key(p: Path) -> Tuple[int, int]:
    st = p.stat()
    return st.st_ino, st.st_dev

def load_flake8_from_toml(filename: Path) -> Dict[str, Any]:
    try:
        with filename.open('rb') as f:
            settings = toml.load(f)
        if 'tool' in settings and 'flake8' in settings['tool']:
            return {"flake8": settings["tool"]["flake8"]}
        else:
            return {}
    except Exception:
        return {}

def normalize_from_toml(settings: Dict[str, Any]) -> Dict[str, Any]:
    output = {}
    for key, value in settings["flake8"].items():
        if isinstance(value, (bool, int, float)):
            value = str(value)
        elif isinstance(value, list):
            value = ",".join(str(x) for x in value)
        output[key] = value
    return {"flake8": output}

def find_and_load_toml_file(_path: Optional[str]=None) -> Tuple[Optional[Path], Dict[str, Any]]:
    if _path:
        path = Path(_path).resolve()
    else:
        path = Path(".").resolve()

    cfg_path = path / "pyproject.toml"
    if cfg_path.exists():
        cfg = load_flake8_from_toml(cfg_path)
        if cfg:
            return cfg_path, cfg

    # did not find any configuration file
    return None, {}

def monkeypatch():
    flake8_parse_config = flake8.options.config.parse_config
    flake8_option_manager = flake8.options.config.OptionManager

    def parse_config(
        option_manager: flake8_option_manager,
        cfg: configparser.RawConfigParser,
        cfg_dir: str,
    ) -> Dict[str, Any]:
        _cfg_path, loaded_toml = find_and_load_toml_file()
        if loaded_toml:
            normalized = normalize_from_toml(loaded_toml)
            cfg.read_dict(normalized)
        return flake8_parse_config(option_manager, cfg, cfg_dir)

    flake8.options.config.parse_config = parse_config
