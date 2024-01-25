from gendiff.compartion import compare_file
from gendiff.parser import get_data
from gendiff.formatters.formater import apply_format


def generate_diff(path1, path2, format='stylish'):
    data1 = get_data(path1)
    data2 = get_data(path2)
    diff = compare_file(data1, data2)
    return apply_format(diff, format)
