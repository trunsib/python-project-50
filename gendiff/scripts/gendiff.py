#!/usr/bin/env python3
from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.main import parser_arg


def main():
    filepath1, filepath2, format_name = parser_arg()
    diff = generate_diff(filepath1, filepath2, format_name)
    print(diff)


if __name__ == "__main__":
    main()
