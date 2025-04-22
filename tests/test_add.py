import unittest
from src.add import add


class TestAdd(unittest.TestCase):
    def test_add_empty(self):
        self.assertEqual(add(""), 0)
