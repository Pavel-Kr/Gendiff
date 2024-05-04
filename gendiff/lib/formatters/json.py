import json


indent_level = 4


def to_json(tree):
    return json.dumps(tree, indent=indent_level, sort_keys=True)
