from pathlib import Path

from hexlet_code.scripts.gendiff import generate_diff

TESTDATA = Path(__file__).parent / 'test_data'


def test_generate_diff():
    expected = (TESTDATA / 'expected_plain.txt').read_text().strip()
    assert (generate_diff(TESTDATA / 'yml_file_1.yaml', TESTDATA /
                          'yml_file_2.yaml', format='plain') ==
            expected)


def test_generate_diff_negative():
    expected = """"""
    assert (generate_diff(TESTDATA / 'yml_file_1.yaml', TESTDATA /
                          'yml_file_2.yaml', format='plain')
            != expected)


def test_generate_diff_same_file():
    expected = """"""
    assert (generate_diff(TESTDATA / 'yml_file_1.yaml', TESTDATA /
                          'yml_file_1.yaml', format='plain')
            == expected)


def test_empty_diff():
    expected = """"""
    assert (generate_diff(TESTDATA / 'empty_json1.json',
                         TESTDATA / 'empty_json2.json', format='plain')
            == expected)


def test_generate_diff_plain_yaml():
    expected = (TESTDATA / 'expected_plain.txt').read_text().strip()
    result = generate_diff(
        TESTDATA / 'yml_file_1.yaml',
        TESTDATA / 'yml_file_2.yaml',
        format='plain'
    )
    assert result == expected


def test_generate_diff_plain_same_file():
    result = generate_diff(
        TESTDATA / 'yml_file_1.yaml',
        TESTDATA / 'yml_file_1.yaml',
        format='plain'
    )
    assert result == ''


def test_generate_diff_plain_empty_files():
    result = generate_diff(
        TESTDATA / 'empty_json1.json',
        TESTDATA / 'empty_json2.json',
        format='plain'
    )
    assert result == ''


def test_generate_diff_plain_yaml2():
    expected = (TESTDATA / 'expected_plain.txt').read_text().strip()
    result = generate_diff(
        TESTDATA / 'file1.json',
        TESTDATA / 'yml_file_2.yaml',
        format='plain'
    )
    assert result == expected


def test_generate_diff_plain_same_file2():
    result = generate_diff(
        TESTDATA / 'yml_file_1.yaml',
        TESTDATA / 'file1.json',
        format='plain'
    )
    assert result == ''

