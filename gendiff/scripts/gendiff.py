#!/usr/bin/env python3
from gendiff.parser import parser_arg
from gendiff.generate_diff import generate_diff


def main():

    filepath1, filepath2, format_name = parser_arg()
    diff = generate_diff(filepath1, filepath2, format_name)
    print(diff)


if __name__ == "__main__":
    
    main()
