from gendiff.compartion import build_diff
from gendiff.parser import get_data
from gendiff.formater import apply_format


def generate_diff(path1, path2, format='stylish'):
    data1 = get_data(path1)
    data2 = get_data(path2)
    diff = build_diff(data1, data2)
    return apply_format(diff, format)
