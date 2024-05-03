action_to_sign = {
    'keep': ' ',
    'remove': '-',
    'add': '+'
}

spaces_per_indent = 4


def _decorate_value(value, depth):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return str(value)

    current_indent = depth * spaces_per_indent
    deeper_indent = (depth + 1) * spaces_per_indent
    strings = ['{']
    spaces = ' ' * deeper_indent
    for key, val in value.items():
        new_val = _decorate_value(val, depth + 1)
        strings.append(f'{spaces}{key}: {new_val}')
    strings.append(' ' * current_indent + '}')
    return '\n'.join(strings)


def to_stylish(tree: dict) -> str:
    offset_to_left = 2

    def walk(diff: dict, depth):
        current_indent = depth * spaces_per_indent
        deeper_indent = (depth + 1) * spaces_per_indent
        diff_list = ['{']
        for key in sorted(diff.keys()):
            val = diff[key]
            if 'action' in val.keys():
                action = val['action']
                spaces = ' ' * (deeper_indent - offset_to_left)
                if action == 'changed':
                    old_value = _decorate_value(val['old_value'], depth + 1)
                    new_value = _decorate_value(val['new_value'], depth + 1)
                    diff_list.append(f'{spaces}- {key}: {old_value}')
                    diff_list.append(f'{spaces}+ {key}: {new_value}')
                else:
                    sign = action_to_sign[action]
                    value = _decorate_value(val['value'], depth + 1)
                    diff_list.append(f'{spaces}{sign} {key}: {value}')
            elif 'children' in val.keys():
                children = val['children']
                spaces = ' ' * deeper_indent
                value = walk(children, depth + 1)
                diff_list.append(f'{spaces}{key}: {value}')
        diff_list.append((' ' * current_indent) + '}')
        result = '\n'.join(diff_list)
        return result

    return walk(tree, 0)
