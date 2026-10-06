import pytest
from hexlet_code.scripts.gendiff import json_reader
from pathlib import Path

TESTDATA = Path(__file__).parent / 'testdata'




def test_keys_file1():
    expected = ['host', 'timeout', 'proxy', 'follow']
    assert list(json_reader(TESTDATA / 'file1.json').keys()) == expected

def test_keys_file2():
    expected = ['timeout', 'verbose', 'host']
    assert list(json_reader(TESTDATA / 'file2.json').keys()) == expected

def test_values_file1():
    expected = ['hexlet.io', 50, '123.234.53.22', False]
    assert list(json_reader(TESTDATA / 'file1.json').values()) == expected

def test_values_file2():
    expected = [20, True, 'hexlet.io']
    assert list(json_reader(TESTDATA / 'file2.json').values()) == expected

def test_read_file1():
    expected = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}
    assert json_reader(TESTDATA / 'file1.json') == expected
