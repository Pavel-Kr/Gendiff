import json
import yaml


def parse_file(file_path: str) -> str:
    with open(file_path) as file:
        if file_path.endswith(('.yaml', '.yml')):
            res = yaml.load(file, Loader=yaml.CLoader)
        elif file_path.endswith('.json'):
            res = json.load(file)
    return res
