from gendiff.data import get_dict_from_file
from gendiff.diff import diff
from gendiff.formats.format import format_diff


def generate_diff(filepath1, filepath2, format_name='stylish'):
    d1 = get_dict_from_file(filepath1)
    d2 = get_dict_from_file(filepath2)
    l_diff = diff(d1, d2)
    return format_diff(l_diff, format_name)
