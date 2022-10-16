#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class that defines test cases for the max_integer function"""

    def test_largest_element(self):
        """Test whether the received aargument is of type list"""
        self.assertEqual(max_integer([1, 2, 5, 9]), 9)
        self.assertEqual(max_integer([1.2, 5.3, 5.364, 2]), 5.364)
        self.assertEqual(max_integer(['a', 'g', 't']), 't')
        self.assertEqual(max_integer("We ni J mi ni nare"), 'r')
        self.assertEqual(max_integer((1, 3, 12, 54)), 54)
        self.assertEqual(max_integer(',.;/'), ';')

    def test_values(self):
        """Make sure right errors are raised for wrong data types passed"""

        self.assertRaises(TypeError, max_integer, 12)
