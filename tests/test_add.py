import unittest
from src.add import add


class TestAdd(unittest.TestCase):
    def test_add_empty(self):
        self.assertEqual(add(""), 0)

    def test_add_one_number(self):
        self.assertEqual(add("1"), 1)
    
    def test_multiple_numbers(self):
        self.assertEqual(add("1,5"), 6)