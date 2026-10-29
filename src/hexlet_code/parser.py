import json
import yaml
from pathlib import Path

def parser(file_path):
    path = Path(file_path)
    end_of_name = path.suffix

    if end_of_name == ".json":
        return pars_json(file_path)
    elif end_of_name in ('.yaml', '.yml'):
        return pars_yaml(file_path)

def pars_json(file_path):
    with open(file_path) as f:
        return json.load(f)

def pars_yaml(file_path):
    with open(file_path) as f:
        return yaml.safe_load(f)