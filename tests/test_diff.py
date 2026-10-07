from pathlib import Path

from hexlet_code.scripts.gendiff import generate_diff

TESTDATA = Path(__file__).parent / 'testdata'

def test_generate_diff():
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    assert generate_diff(TESTDATA / 'file1.json', TESTDATA / 'file2.json') == expected

def test_generate_diff_negative():
    expected = """{"""
    assert generate_diff(TESTDATA / 'file1.json', TESTDATA / 'file2.json') != expected


def test_generate_diff_same_file():
    expected = """{
    follow: false
    host: hexlet.io
    proxy: 123.234.53.22
    timeout: 50
}"""
    assert generate_diff(TESTDATA / 'file1.json',TESTDATA / 'file1.json') == expected

def test_empty_diff():
    expected = """{}"""
    assert generate_diff(TESTDATA / 'empty_json1.json', TESTDATA / 'empty_json2.json') == expected