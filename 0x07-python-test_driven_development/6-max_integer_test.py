#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer  # Importing the max_integer function

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_normal_cases(self):
        """Test normal lists of integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3]), -1)
        self.assertEqual(max_integer([100, 200, 150]), 200)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        """Test a list with one element"""
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([-5]), -5)

    def test_floats(self):
        """Test a list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_string_elements(self):
        """Test with a list containing strings (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer(['a', 'b', 'c'])

    def test_mixed_types(self):
        """Test with a list containing mixed types (should raise TypeError)"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3'])

if __name__ == '__main__':
    unittest.main()
