ACTION_TO_SIGN = {
    'keep': ' ',
    'remove': '-',
    'add': '+'
}

SPACES_PER_INDENT = 4
OFFSET_TO_LEFT = 2


def _decorate_value(value, depth):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return str(value)

    current_indent = depth * SPACES_PER_INDENT
    deeper_indent = (depth + 1) * SPACES_PER_INDENT
    strings = ['{']
    spaces = ' ' * deeper_indent
    for key, val in value.items():
        new_val = _decorate_value(val, depth + 1)
        strings.append(f'{spaces}{key}: {new_val}')
    strings.append(' ' * current_indent + '}')
    return '\n'.join(strings)


def _walk(diff: dict, depth):
    current_indent = depth * SPACES_PER_INDENT
    deeper_indent = (depth + 1) * SPACES_PER_INDENT
    diff_list = ['{']
    for key in sorted(diff.keys()):
        val = diff[key]
        action = val['action']
        spaces = ' ' * (deeper_indent - OFFSET_TO_LEFT)
        if action == 'changed':
            old_value = _decorate_value(val['old_value'], depth + 1)
            new_value = _decorate_value(val['new_value'], depth + 1)
            diff_list.append(f'{spaces}- {key}: {old_value}')
            diff_list.append(f'{spaces}+ {key}: {new_value}')
        elif action == 'nested':
            children = val['value']
            spaces = ' ' * deeper_indent
            value = _walk(children, depth + 1)
            diff_list.append(f'{spaces}{key}: {value}')
        else:
            sign = ACTION_TO_SIGN[action]
            value = _decorate_value(val['value'], depth + 1)
            diff_list.append(f'{spaces}{sign} {key}: {value}')

    diff_list.append((' ' * current_indent) + '}')
    result = '\n'.join(diff_list)
    return result


def convert_to_stylish(tree: dict) -> str:
    return _walk(tree, 0)
