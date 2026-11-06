from pathlib import Path

from gendiff.scripts.gendiff import generate_diff

TESTDATA = Path(__file__).parent / 'test_data'


def test_generate_diff():
    expected = (TESTDATA / 'expected_json_format.json').read_text().strip()
    assert (generate_diff(TESTDATA / 'yml_file_1.yaml', TESTDATA /
                          'yml_file_2.yaml', format='json') ==
            expected)


def test_generate_diff_json_yaml():
    expected = (TESTDATA / 'expected_json_format.json').read_text().strip()
    result = generate_diff(
        TESTDATA / 'yml_file_1.yaml',
        TESTDATA / 'yml_file_2.yaml',
        format='json'
    )
    assert result == expected


def test_generate_diff_json_same_file():
    expected = (TESTDATA / 'unchanged_json.json').read_text().strip()
    result = generate_diff(
        TESTDATA / 'yml_file_1.yaml',
        TESTDATA / 'yml_file_1.yaml',
        format='json'
    )
    assert result == expected


def test_generate_diff_json_empty_files():
    result = generate_diff(
        TESTDATA / 'empty_json1.json',
        TESTDATA / 'empty_json2.json',
        format='json'
    )
    assert result == '[]'


def test_generate_diff_json_yaml2():
    expected = (TESTDATA / 'expected_json_format.json').read_text().strip()
    result = generate_diff(
        TESTDATA / 'file1.json',
        TESTDATA / 'yml_file_2.yaml',
        format='json'
    )
    assert result == expected


def test_generate_diff_json_same_file2():
    expected = (TESTDATA / 'unchanged_json.json').read_text().strip()
    result = generate_diff(
        TESTDATA / 'yml_file_1.yaml',
        TESTDATA / 'file1.json',
        format='json'
    )
    assert result == expected


def test_generate_diff_bool_vs_int_json():
    expected = """[
  {
    "status": "changed",
    "key": "value",
    "old_value": false,
    "new_value": 0
  }
]"""
    result = generate_diff(
        TESTDATA / 'file_with_zero.json',
        TESTDATA / 'file_with_zero2.json',
        format='json'
    )
    assert result == expected

