import pytest

from greet_app.greet import greet


@pytest.mark.parametrize("test_input,expected", [("Bob", "Hello, Bob."), ("JERRY", "HELLO JERRY!"),
                                                 (None, "Hello, my friend.")])
def test_greet_with_one_name(test_input, expected):
    assert greet(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(["Jill", "Jane"], "Hello, Jill and Jane."),
                                                 (("Mike", "James"), "Hello, Mike and James."),
                                                 (["Amy", "Brian", "Charlotte"], "Hello, Amy, Brian and Charlotte."),
                                            (["Amy", "BRIAN", "Charlotte"], "Hello, Amy and Charlotte. AND HELLO BRIAN!"),
                                                 (["Amy", "BRIAN", "Charlotte", "JERRY"],
                                                  "Hello, Amy and Charlotte. AND HELLO BRIAN and JERRY!")])
def test_greet_with_two_names_from_arr(test_input, expected):
    assert greet(test_input) == expected

