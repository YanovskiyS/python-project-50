from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.json import json_format


class ErrorFormat(Exception):
    pass


def apply_format(diff_result, data_format):
    if data_format == 'stylish':
        return stylish_format(diff_result)
    if data_format == 'plain':
        return plain_format(diff_result)
    if data_format == 'json':
        return json_format(diff_result)
    raise ErrorFormat(f"Unknown format!: {data_format}")
