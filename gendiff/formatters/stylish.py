import itertools
REPLACER = '  '
INDENT = '    '


class ErrorUnknownOperation(Exception):
    pass


def make_space(indent, depth):
    return indent * depth


def value_to_str(value, depth):
    if isinstance(value, dict):
        result = []
        for key, value in value.items():
            space = make_space(INDENT, depth + 1)
            result.append(f"\n{space}{key}: {value_to_str(value, depth + 1)}")
        line = itertools.chain('{', result, '\n', [INDENT * depth, '}'])
        return ''.join(line)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def build_line(data, key, depth, INDENT='  '):
    space = make_space(REPLACER, depth)
    return f"{space}{INDENT}{data['key']}: " \
           f"{value_to_str(data[key], depth+1)}"


def walk(node, depth=0):    # noqa: C901
    lines = []
    space = make_space(REPLACER, depth + 1)
    for value in node.values():
        if value['operation'] == 'nested':
            lines.append(f"{space * 2}{value['key']}: "
                         f"{walk(value['value'], depth + 1)}")
            continue
        if value['operation'] == 'changed':
            lines.append(f"{space}{build_line(value, 'old', depth, '- ')}")
            lines.append(f"{space}{build_line(value, 'new', depth, '+ ')}")
            continue
        if value['operation'] == 'deleted':
            lines.append(f"{space}{build_line(value, 'value', depth, '- ')}")
            continue
        if value['operation'] == 'added':
            lines.append(f"{space}{build_line(value, 'value', depth, '+ ')}")
            continue
        if value['operation'] == 'unchanged':
            lines.append(f"{space}{build_line(value, 'value', depth)}")
            continue
        else:
            raise ErrorUnknownOperation(f"Unknown operation!:"
                                        f"{value['operation']}")

    result = itertools.chain('{', lines, [INDENT * depth + '}'])
    return "\n".join(result)


def stylish_format(diff_result):
    return walk(diff_result)
