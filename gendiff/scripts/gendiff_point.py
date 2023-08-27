#!/usr/bin/env python3

"""A script that runs a main function in terminal."""

import argparse


def main():
    """A function that creates description in terminal."""
    parser = argparse.ArgumentParser(
        description='Compares two configuration '
                    'files and shows a difference.'
    )
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        type=str,
                        help='set format of output',
                        default='stylish')
    args = parser.parse_args()

    print(args.first_file, args.second_file, args.format)


if __name__ == '__main__':
    main()
