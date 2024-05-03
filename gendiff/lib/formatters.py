def stylish(tree: dict) -> str:
    spaces_per_indent = 4
    offset_to_left = 2

    def stylish_value(value, depth) -> str:
        current_indent = depth * spaces_per_indent
        deeper_indent = (depth + 1) * spaces_per_indent

        if isinstance(value, dict):
            strings = ['{']
            for key, val in value.items():
                spaces = ' ' * deeper_indent
                strings.append(f'{spaces}{key}: {stylish_value(val, depth + 1)}')
            spaces = ' ' * current_indent
            strings.append(spaces + '}')
            return '\n'.join(strings)
        else:
            return str(value)

    def walk(diff: dict, depth):
        current_indent = depth * spaces_per_indent
        deeper_indent = (depth + 1) * spaces_per_indent
        diff_list = ['{']
        for key in sorted(diff.keys()):
            for data in diff[key]:
                if 'value' in data:
                    action = data['action']
                    value = data['value']
                    spaces = ' ' * (deeper_indent - offset_to_left)
                    diff_list.append(f'{spaces}{action} {key}: {stylish_value(value, depth + 1)}')
                elif 'children' in data:
                    children = data['children']
                    spaces = ' ' * deeper_indent
                    value = walk(children, depth + 1)
                    diff_list.append(f'{spaces}{key}: {value}')
        diff_list.append((' ' * current_indent) + '}')
        result = '\n'.join(diff_list)
        return result

    return walk(tree, 0)
