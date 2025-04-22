import unittest
from src.add import add


class TestAdd(unittest.TestCase):
    def test_add_empty(self):
        self.assertEqual(add(""), 0)

    def test_add_one_number(self):
        self.assertEqual(add("1"), 1)

    def test_add_multiple_numbers(self):
        self.assertEqual(add("1,5"), 6)

    def test_add_multiple_numbers_newline(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_add_different_delimter(self):
        self.assertEqual(add("//;\n1;2"), 3)
        self.assertEqual(add("//\t\n1\t2,3\t4"), 10)
        self.assertEqual(add("//@\n1@2,3@4"), 10)

    def test_add_individual_negative_number(self):
        with self.assertRaises(Exception) as cm:
            add("-1,2")
        self.assertEqual(str(cm.exception), "negative numbers not allowed -1")

    def test_add_multiple_negative_number(self):
        with self.assertRaises(Exception) as cm:
            add("-1,-2,3,-4")
        self.assertEqual(str(cm.exception), "negative numbers not allowed -1,-2,-4")

        with self.assertRaises(Exception) as cm:
            add("-1,-2,4,5")
        self.assertEqual(str(cm.exception), "negative numbers not allowed -1,-2")

        with self.assertRaises(Exception) as cm:
            add("//\t\n1\t-2,3\t4")
        self.assertEqual(str(cm.exception), "negative numbers not allowed -2")
