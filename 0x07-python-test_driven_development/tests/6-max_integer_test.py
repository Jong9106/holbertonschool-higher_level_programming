#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_maxint(self):
        """ Different type of list """
        # List of 3 elements
        self.assertEqual(max_integer([80, 9, 6]), 80)
        # Only one element
        self.assertEqual(max_integer([60]), 60)
        # All elements are the same
        self.assertEqual(max_integer([6, 6, 6]), 6)
        # With float elements
        self.assertEqual(max_integer([3.5, 6.9, 7.1]), 7.1)
        # With negative numbers
        self.assertEqual(max_integer([-4, -77, 0, -8, -5]), 0)

    def text_emptylist(self):
        """ void list"""
        self.assertEqual(max_integer([]), None)

    def test_typeserror(self):
        """Test errors values"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, (3 + 6j))
