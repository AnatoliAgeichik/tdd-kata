import pytest

from greet_app.greet import greet


@pytest.mark.parametrize("test_input,expected", [("Bob", "Hello, Bob."), ("JERRY", "HELLO JERRY!"),
                                                 (None, "Hello, my friend.")])
def test_greet_with_one_name(test_input, expected):
    assert greet(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(["Jill", "Jane"], "Hello, Jill and Jane."),
                                                 (("Mike", "James"), "Hello, Mike and James."),
                                                 (["Amy", "Brian", "Charlotte"], "Hello, Amy, Brian and Charlotte."),
                                                 (["Amy", "BRIAN", "Charlotte"],
                                                  "Hello, Amy and Charlotte. AND HELLO BRIAN!"),
                                                 (["Amy", "BRIAN", "Charlotte", "JERRY"],
                                                  "Hello, Amy and Charlotte. AND HELLO BRIAN and JERRY!")])
def test_greet_with_two_names_from_arr(test_input, expected):
    assert greet(test_input) == expected


@pytest.mark.parametrize("test_input,expected", [(["Bob", "Charlie, Dianne"], "Hello, Bob, Charlie and Dianne."),
                                                 (["Amy, BRIAN, Charlotte, JERRY"],
                                                  "Hello, Amy and Charlotte. AND HELLO BRIAN and JERRY!"),
                                                 ("Amy, BRIAN, Charlotte, JERRY",
                                                  "Hello, Amy and Charlotte. AND HELLO BRIAN and JERRY!"),
                                                 (["Bob", "\"Charlie, Dianne\"", "Jane"],
                                                  "Hello, Bob, Charlie, Dianne and Jane."),
                                                 (["Bob", "\"Charlie, Dianne\""],
                                                  "Hello, Bob and Charlie, Dianne."),
                                                 (["\"Charlie, Dianne\"", "Jane"],
                                                  "Hello, Charlie, Dianne and Jane."),
                                                 ])
def test_greet_with_string_containing_comma(test_input, expected):
    assert greet(test_input) == expected

