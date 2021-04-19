import pytest

from greet_app.greet import greet


def test_greet_with_name():
    data = "Bob"
    result = greet(data)
    expected = "Hello, {}.".format(data)
    assert result == expected


def test_greet_without_name():
    data = None
    result = greet(data)
    expected = "Hello, my friend."
    assert result == expected