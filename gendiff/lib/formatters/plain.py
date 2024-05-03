def decorate_value(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, (dict, list)):
        return '[complex value]'
    return repr(value)


def walk(diff: dict, path: str):
    diff_list = []
    for key in sorted(diff.keys()):
        val = process_key(diff, key, path)
        diff_list.append(val)
    return diff_list


def process_key(diff: dict, key: str, path: str) -> str:
    prop = path + key
    val = diff[key]
    if 'action' in val.keys():
        action = val['action']
        if action == 'add':
            value = decorate_value(val['value'])
            return f"Property '{prop}' was added with value: {value}"
        elif action == 'remove':
            return f"Property '{prop}' was removed"
        elif action == 'changed':
            old_value = decorate_value(val['old_value'])
            new_value = decorate_value(val['new_value'])
            return f"Property '{prop}' was updated. " \
                   f"From {old_value} to {new_value}"
    elif 'children' in val.keys():
        children = val['children']
        res = [item for item in walk(children, prop + '.') if item]
        return '\n'.join(res)


def to_plain(tree: dict):
    res = walk(tree, '')
    return '\n'.join(res)
