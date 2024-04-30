import json
from collections import defaultdict


_KEEP = ' '
_REMOVE = '-'
_ADD = '+'


def generate_diff(file_path_1, file_path_2):
    with (
        open(file_path_1, 'r') as file_1,
        open(file_path_2, 'r') as file_2
    ):
        json_1 = json.load(file_1)
        json_2 = json.load(file_2)
        diff = defaultdict(list)
        key_set_1 = set(json_1)
        key_set_2 = set(json_2)
        for key in key_set_1 - key_set_2:
            diff[key].append((json_1[key], _REMOVE))
        for key in key_set_2 - key_set_1:
            diff[key].append((json_2[key], _ADD))
        for key in key_set_1 & key_set_2:
            if json_1[key] == json_2[key]:
                diff[key].append((json_1[key], _KEEP))
            else:
                diff[key].append((json_1[key], _REMOVE))
                diff[key].append((json_2[key], _ADD))
        diff_list = []
        for key in sorted(diff.keys()):
            for value, action in diff[key]:
                diff_list.append(f'{action} {key}: {value}')
        result = '{\n\t' + '\n\t'.join(diff_list) + '\n}'
        return result
