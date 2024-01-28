from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format



def get_format(diff_result, format):
    if format == 'stylish':
        return stylish_format(diff_result)
    if format == 'plain':
        return plain_format(diff_result)