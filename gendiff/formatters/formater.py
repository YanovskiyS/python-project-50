from gendiff.formatters.stylish import stylish_format


def apply_format(diff_result, format):
    if format == 'stylish':
        return stylish_format(diff_result)
