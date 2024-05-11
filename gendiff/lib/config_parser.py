import json
import yaml


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        text = file.read()
        return text


def parse_content(text: str, ext: str) -> str:
    if ext == '.yaml' or ext == '.yml':
        res = yaml.load(text, Loader=yaml.CLoader)
    elif ext == '.json':
        res = json.loads(text)
    return res
