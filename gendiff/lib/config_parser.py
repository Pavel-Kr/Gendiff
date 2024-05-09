import json
import yaml
from os.path import splitext


def read_file(file_path: str) -> str:
    with open(file_path) as file:
        text = file.read()
        return text


def parse_file(file_path: str) -> str:
    text = read_file(file_path)
    _, ext = splitext(file_path)
    if ext == '.yaml' or ext == '.yml':
        res = yaml.load(text, Loader=yaml.CLoader)
    elif ext == '.json':
        res = json.loads(text)
    return res
