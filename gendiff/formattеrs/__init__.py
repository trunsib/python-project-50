from gendiff.formattеrs.stylish import stylish
from gendiff.formattеrs.plain import plain
from gendiff.formattеrs.json import json


def format_diff(diff_data, format_name='stylish'):
    """Apply the specified formatter to the diff data."""
    if format_name == 'stylish':
        return stylish(diff_data)
    elif format_name == 'plain':
        return plain(diff_data)
    elif format_name == 'json':
        return json(diff_data)
    else:
        raise ValueError(f'Unknown format: {format_name}')
    