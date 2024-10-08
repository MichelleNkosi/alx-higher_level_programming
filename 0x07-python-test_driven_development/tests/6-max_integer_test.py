#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_max_at_middle(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_one_element(self):
        self.assertEqual(max_integer(), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_all_same_numbers(self):
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

if __name__ == '__main__':
    unittest.main()
