import unittest
import sys
sys.path.insert(0, '../greet_app/')

from greet import greet


class TestGreet(unittest.TestCase):

    def test_greet_with_name(self):
        data = "Bob"
        result = greet(data)
        expected = "Hello, Bob."
        self.assertEqual(result, expected)
    
    