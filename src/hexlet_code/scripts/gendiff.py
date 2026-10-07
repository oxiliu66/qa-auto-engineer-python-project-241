import argparse
import json


def json_reader(file):
    with open(file) as f:
        return json.load(f)


def format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return str(value)


def generate_diff(file1, file2):
    data1 = json_reader(file1)
    data2 = json_reader(file2)
    result = []
    all_keys = sorted(set(data1) | set(data2))

    for key in all_keys:
        if key in data1 and key in data2:
            if data1[key] == data2[key]:
                result.append(f'    {key}: {format_value(data1[key])}')
            else:
                result.append(f'  - {key}: {format_value(data1[key])}')
                result.append(f'  + {key}: {format_value(data2[key])}')
        elif key in data1:
            result.append(f'  - {key}: {format_value(data1[key])}')
        else:
            result.append(f'  + {key}: {format_value(data2[key])}')

    if not result:
        return '{}'
    return '{\n' + '\n'.join(result) + '\n}'


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