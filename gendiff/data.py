from pathlib import Path
import os
import json
import yaml

def get_dict_from_file(filepath):
    path = Path(filepath)
    if not path.exists():
        path = Path.cwd() / 'tests' / 'fixtures' / os.path.basename(filepath)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {filepath!s} (tried {path!s})")

    suffix = path.suffix.lower()
    with open(path, 'r') as f:
        if suffix == '.json':
            return json.load(f)
        if suffix in ('.yml', '.yaml'):
            return yaml.safe_load(f)
        raise ValueError(f"Unsupported file format: {suffix}")