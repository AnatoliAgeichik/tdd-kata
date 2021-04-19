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


def test_greet_with_uppercase_name():
    data = "JERRY"
    result = greet(data)
    expected = "HELLO {}!".format(data)
    assert result == expected


def test_greet_with_two_names_from_list():
    data = ["Jill", "Jane"]
    result = greet(data)
    expected = "Hello, Jill and Jane."
    assert result == expected
