#!/usr/bin/env python3
import argparse
from gendiff import generate_diff
from gendiff.lib.formatters import stylish


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format for output',
                        default='stylish')
    args = parser.parse_args()
    if args.format == 'stylish':
        formatter = stylish
    diff = generate_diff(args.first_file, args.second_file, formatter)
    print(diff)


if __name__ == '__main__':
    main()
