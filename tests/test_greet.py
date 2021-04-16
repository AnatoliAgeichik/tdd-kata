import unittest

from greet_app.greet import greet


class TestGreet(unittest.TestCase):

    def test_greet_with_name(self):
        data = "Bob"
        result = greet(data)
        expected = "Hello, {}.".format(data)
        self.assertEqual(result, expected)

    def test_greet_without_name(self):
        data = None
        result = greet(data)
        expected = "Hello, my friend."
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
 