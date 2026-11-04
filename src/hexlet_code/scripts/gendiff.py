import argparse
import json

from hexlet_code.diff_generate import build_diff
from hexlet_code.formatters.json import format_json
from hexlet_code.formatters.plain import format_plain
from hexlet_code.formatters.stylish import format_style
from hexlet_code.parser import parser


def json_reader(file):
    with open(file) as f:
        return json.load(f)


def generate_diff(file1, file2, format='stylish'):
    data1 = parser(file1)
    data2 = parser(file2)
    diff = build_diff(data1, data2)
    if format == 'stylish':
        return format_style(diff)
    elif format == 'plain':
        return format_plain(diff)
    elif format == 'json':
        return format_json(diff)
    else:
        raise ValueError(f'Unknown format: {format}')


def main():  # pragma: no cover
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish',
                        help='set format of output')
    args = parser.parse_args()

    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':  # pragma: no cover
    main()