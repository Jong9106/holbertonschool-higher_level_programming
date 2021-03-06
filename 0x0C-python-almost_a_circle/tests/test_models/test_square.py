#!/usr/bin/python3
"""Unittest for square.py"""


import unittest
import json
import io
import inspect
from contextlib import redirect_stdout
from models.base import Base, __doc__
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    Testing for Square class
    """
    def test_docstring(self):
        """
        testing docstring
        """
        self.assertIsNotNone(Square.__doc__)

    def test_init(self):
        """
        Testing init
        """
        t1 = Square(8, 10, 10, 15)
        self.assertEqual(t1.width, 8)
        self.assertEqual(t1.height, 8)
        self.assertEqual(t1.x, 10)
        self.assertEqual(t1.y, 10)
        self.assertEqual(t1.id, 15)

    def test_init2(self):
        """
        testing init with just height and width
        """
        t1 = Square(10)
        self.assertEqual(t1.width, 10)
        self.assertEqual(t1.height, 10)
        self.assertEqual(t1.x, 0)
        self.assertEqual(t1.y, 0)

    def test_not_int(self):
        """
        testing if not int
        """
        with self.assertRaises(TypeError):
            Square("Yo")

    def test_negative(self):
        """
        testing negative
        """
        with self.assertRaises(ValueError):
            Square(-50)

    def test_zero(self):
        """
        testing zero
        """
        with self.assertRaises(ValueError):
            Square(0)

    def test_x_int(self):
        """
        testing x is not int
        """
        with self.assertRaises(TypeError):
            Square(2, "Yo")

    def test_x_int(self):
        """
        testing x is negative
        """
        with self.assertRaises(ValueError):
            Square(2, -5)

    def test_y_int(self):
        """
        testing y is not int
        """
        with self.assertRaises(TypeError):
            Square(2, 5, "Yo")

    def test_y_int(self):
        """
        testing y is negative
        """
        with self.assertRaises(ValueError):
            Square(2, 5, -5)

    def test_area(self):
        """
        testing area works with just 2 arguments
        """
        t1 = Square(10)
        self.assertEqual(t1.area(), 100)

    def test_area2(self):
        """
        testing area works with all arguments
        """
        t1 = Square(5, 3, 5, 15)
        self.assertEqual(t1.area(), 25)

    def test_displayx5(self):
        """
        Testing display
        """
        r1 = Square(5, 5, 5, 5)
        display = ('\n' * 5 + (((' ' * 5) + '#' * 5 + '\n') * 5))
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        out = f.getvalue()
        self.assertEqual(out, display)

    def test_str_return(self):
        """
        testing the str returns right
        """
        t1 = Square(4, 2, 1, 12)
        self.assertEqual(t1.__str__(), "[Square] (12) 2/1 - 4")

    def test_display(self):
        """
        Testing display
        """
        r1 = Square(2, 2, 2, 2)
        display = ('\n' * 2 + (((' ' * 2) + '#' * 2 + '\n') * 2))
        f = io.StringIO()
        with redirect_stdout(f):
            r1.display()
        out = f.getvalue()
        self.assertEqual(out, display)

    def test_size_setter(self):
        """
        testing size setts work
        """
        t1 = Square(4, 2, 1, 12)
        t1.size = 20
        self.assertEqual(t1.__str__(), "[Square] (12) 2/1 - 20")

    def test_size_fail(self):
        """
        testing size setter fail
        """
        t1 = Square(4, 2, 1, 12)
        with self.assertRaises(TypeError):
            t1.size = "yo"
        with self.assertRaises(ValueError):
            t1.size = -20

    def test_update(self):
        """
        testing update works right
        """
        t1 = Square(10, 10, 10, 10)
        t1.update(89)
        self.assertEqual(t1.__str__(), "[Square] (89) 10/10 - 10")
        t1.update(89, 2)
        self.assertEqual(t1.__str__(), "[Square] (89) 10/10 - 2")
        t1.update(89, 2, 3)
        self.assertEqual(t1.__str__(), "[Square] (89) 10/10 - 2")
        t1.update(89, 2, 3, 4)
        self.assertEqual(t1.__str__(), "[Square] (89) 4/10 - 2")

    def test_update_size_check(self):
        """
        testing update checks size validation
        """
        t1 = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            t1.update(89, "Yo", 3, 4)
        with self.assertRaises(ValueError):
            t1.update(89, -5, 3, 4)
        with self.assertRaises(ValueError):
            t1.update(89, 0, 3, 4)

    def test_update_x_check(self):
        """
        testing update checks x validation
        """
        t1 = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            t1.update(89, 3, "Yo", 5)
        with self.assertRaises(ValueError):
            t1.update(89, 5, -4, 5)

    def test_update_y_check(self):
        """
        testing update checks y validation
        """
        t1 = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            t1.update(89, 3, 4, "yo")
        with self.assertRaises(ValueError):
            t1.update(89, 5, 4, -5)

    def test_update_kwargs_check(self):
        """
        testing kwars update works
        """
        t1 = Square(10, 10, 10, 10)
        t1.update(size=1)
        self.assertEqual(t1.__str__(), "[Square] (10) 10/10 - 1")
        t1.update(size=2, x=2)
        self.assertEqual(t1.__str__(), "[Square] (10) 2/10 - 2")
        t1.update(y=1, size=2, x=3, id=89)
        self.assertEqual(t1.__str__(), "[Square] (89) 3/1 - 2")

    def test_update_kwargs_with_args(self):
        """
        testing args exist it ignores kwargs
        """
        t1 = Square(10, 10, 10, 10)
        t1.update(24, 3, x=10)
        self.assertEqual(t1.__str__(), "[Square] (24) 10/10 - 3")

    def test_dictionary_check(self):
        """
        testing the dictionary
        """
        dic = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        t1 = Square(10, 2, 1, 1)
        self.assertEqual(dic, t1.to_dictionary())

    def tearDown(self):
        """ Resset module for id """

        Base._Base__nb_objects = 0
