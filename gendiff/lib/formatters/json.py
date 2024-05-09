import json


INDENT_LEVEL = 4


def convert_to_json(tree):
    return json.dumps(tree, indent=INDENT_LEVEL, sort_keys=True)
