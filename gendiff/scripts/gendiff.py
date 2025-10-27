#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.parser import parser_arg


def main():
    path_file1, path_file2, format_name = parser_arg()
    diff = generate_diff(path_file1, path_file2, format_name)
    print(diff)


if __name__ == '__maine__':
    main()
