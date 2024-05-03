from collections import defaultdict
from gendiff.lib.config_parser import parse_file
from gendiff.lib.formatters import stylish


_KEEP = ' '
_REMOVE = '-'
_ADD = '+'


def build_diff(config_1: dict, config_2: dict) -> dict:
    diff = defaultdict(list)
    key_set_1 = set(config_1)
    key_set_2 = set(config_2)
    for key in key_set_1 - key_set_2:
        diff[key].append({'action': _REMOVE, 'value': config_1[key]})
    for key in key_set_2 - key_set_1:
        diff[key].append({'action': _ADD, 'value': config_2[key]})
    for key in key_set_1 & key_set_2:
        if isinstance(config_1[key], dict) and isinstance(config_2[key], dict):
            nested_diff = build_diff(config_1[key], config_2[key])
            diff[key].append({'children': nested_diff})
        elif config_1[key] == config_2[key]:
            diff[key].append({'action': _KEEP, 'value': config_1[key]})
        else:
            diff[key].append({'action': _REMOVE, 'value': config_1[key]})
            diff[key].append({'action': _ADD, 'value': config_2[key]})
    return diff


def generate_diff(file_path_1: str, file_path_2: str, formatter=stylish):
    config_1 = parse_file(file_path_1)
    config_2 = parse_file(file_path_2)
    diff = build_diff(config_1, config_2)
    result = formatter(diff)
    return result
