import json
from textwrap import indent

def read_json(path):
    with open(path) as f:
        return json.load(f)

def write_json(data, path, indent_level=4):
    with open(path, 'w') as f:
        json.dump(data, f, indent=indent_level)
