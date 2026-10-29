import argparse
import json

from hexlet_code.formatter.diff_generate import build_diff
from hexlet_code.formatter.stylish import format_style
from hexlet_code.parser import parser


def json_reader(file):
    with open(file) as f:
        return json.load(f)


def generate_diff(file1, file2):
    data1 = parser(file1)
    data2 = parser(file2)
    diff = build_diff(data1, data2)
    return format_style(diff)


def main():  # pragma: no cover
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file))


if __name__ == '__main__':  # pragma: no cover
    main()