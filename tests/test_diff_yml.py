from pathlib import Path

from hexlet_code.scripts.gendiff import generate_diff

TESTDATA = Path(__file__).parent / 'test_data'


def test_generate_diff():
    expected = (TESTDATA / 'expected_diff.json').read_text()
    assert (generate_diff(TESTDATA / 'yml_file_1.yaml', TESTDATA /
                          'yml_file_2.yaml') ==
            expected)


def test_generate_diff_negative():
    expected = """{"""
    assert (generate_diff(TESTDATA / 'yml_file_1.yaml', TESTDATA /
                          'yml_file_2.yaml')
            != expected)


def test_generate_diff_same_file():
    expected = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    assert (generate_diff(TESTDATA / 'yml_file_1.yaml', TESTDATA /
                          'yml_file_1.yaml')
            == expected)


def test_empty_diff():
    expected = """{}"""
    assert generate_diff(TESTDATA / 'empty_json1.json',
                         TESTDATA / 'empty_json2.json') == expected
