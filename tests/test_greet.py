import pytest

from greet_app.greet import greet


def test_greet_with_name():
    data = "Bob"
    result = greet(data)
    expected = f"Hello, {data}."
    assert result == expected


def test_greet_without_name():
    data = None
    result = greet(data)
    expected = "Hello, my friend."
    assert result == expected


def test_greet_with_uppercase_name():
    data = "JERRY"
    result = greet(data)
    expected = f"HELLO {data}!"
    assert result == expected


@pytest.mark.parametrize("test_input,expected", [(["Jill", "Jane"], "Hello, Jill and Jane."), (("Mike", "James"),
                                                                                            "Hello, Mike and James.")])
def test_greet_with_two_names_from_arr(test_input, expected):
    assert greet(test_input) == expected
