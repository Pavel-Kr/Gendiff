from collections import defaultdict
from gendiff.lib.config_parser import parse_file


_KEEP = ' '
_REMOVE = '-'
_ADD = '+'


def find_diff(config_1, config_2):
    diff = defaultdict(list)
    key_set_1 = set(config_1)
    key_set_2 = set(config_2)
    for key in key_set_1 - key_set_2:
        diff[key].append((config_1[key], _REMOVE))
    for key in key_set_2 - key_set_1:
        diff[key].append((config_2[key], _ADD))
    for key in key_set_1 & key_set_2:
        if config_1[key] == config_2[key]:
            diff[key].append((config_1[key], _KEEP))
        else:
            diff[key].append((config_1[key], _REMOVE))
            diff[key].append((config_2[key], _ADD))
    return diff


def generate_diff(file_path_1, file_path_2):
    config_1 = parse_file(file_path_1)
    config_2 = parse_file(file_path_2)
    diff = find_diff(config_1, config_2)
    diff_list = []
    for key in sorted(diff.keys()):
        for value, action in diff[key]:
            diff_list.append(f'{action} {key}: {value}')
    result = '{\n\t' + '\n\t'.join(diff_list) + '\n}'
    return result
