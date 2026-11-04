from gendiff.formatters.plain import format_plain_value
from gendiff.formatters.stylish import format_value


def test_format_value():
    assert format_value(True) == "true"
    assert format_value(False) == "false"


def test_format_file_negative():
    assert format_value(1) == "1"


def test_format_file_none():
    assert format_value(None) == "null"


def test_format_value_string():
    assert format_value("hello") == "hello"


def test_format_value_plain():
    assert format_plain_value(True) == "true"
    assert format_plain_value(False) == "false"


def test_format_file_negative_plain():
    assert format_plain_value(1) == "1"


def test_format_file_none_plain():
    assert format_plain_value(None) == "null"


def test_format_value_string_plain():
    assert format_plain_value("hello") == "'hello'"