#!/usr/bin/python3
"""Unittest for Base class"""

import unittest
import json
import pep8
import inspect
from models.base import Base, __doc__
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """ Define TestBase class """
    def test_A_documentation(self):
        """ test class Base documentation in methods and functions """
        self.assertTrue(len(Base.__doc__) > 0)
        func = inspect.getmembers(Base, predicate=inspect.ismethod)
        for name, method in func:
            self.assertTrue(len(method.__doc__) > 0)
        func2 = inspect.getmembers(Base, predicate=inspect.isfunction)
        for name, method in func2:
            self.assertTrue(len(method.__doc__) > 0)

    def test_B_pep8_Base_class(self):
        """
        Test that we conform to PEP8 for base class
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 1, "Found code style errors")

    def test_C_pep8_test_base(self):
        """
        Test that we conform to PEP8 in test for base class
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0, "")

    def test_private_class(self):
        """ here de documentation """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_D_creating_instances(self):
        """
        testing creating instances
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_E_creating_id(self):
        """
        testing creating a instance with a specific ID
        """
        b3 = Base(50)
        self.assertEqual(b3.id, 50)

    def test_F_creating_negative(self):
        """
        testing creating a instance with a negative ID
        """
        b4 = Base(-10)
        self.assertEqual(b4.id, -10)

    def test_G_creating_string(self):
        """
        testing creating a instance with a string ID
        """
        b5 = Base("testing")
        self.assertEqual(b5.id, "testing")

    def test_H_creating_float(self):
        """
        testing creating a instance with a float ID
        """
        b6 = Base(5.2)
        self.assertEqual(b6.id, 5.2)

    def test_I_to_json_string(self):
        """
        testing to_json_string method
        """
        r1 = Rectangle(10, 7, 2, 8)
        dic = r1.to_dictionary()
        new_json_dic = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        json_dic = Base.to_json_string([dic])
        self.assertEqual(dic, new_json_dic)
        self.assertEqual(type(dic), dict)
        self.assertEqual(type(json_dic), str)

    def test_J_to_json_string(self):
        """
        testing to_json_string method empty
        """
        json_dic = Base.to_json_string([])
        self.assertEqual(json_dic, "[]")

    def test_K_json_file_created(self):
        """
        testing json_file method
        """
        t1 = Rectangle(10, 7, 2, 8, 1)
        Rectangle.save_to_file([t1])
        with open("Rectangle.json", "r") as f:
            self.assertEqual([t1.to_dictionary()], json.load(f))

    def test_L_json_file_empty(self):
        """
        testing if file is created with empty
        """
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual([], json.load(f))

    def test_M_save_to_file(self):
        """
        testing the method save_to_file with a Rectangle instance
        """
        rec1 = Rectangle(10, 7, 2, 8)
        rec2 = Rectangle(2, 4)
        json_dic1 = {"id": 1, "height": 7, "width": 10, "y": 8, "x": 2}
        json_dic2 = {"id": 2, "height": 4, "width": 2, "y": 0, "x": 0}
        Rectangle.save_to_file([rec1, rec2])
        with open("Rectangle.json", 'r') as file:
            self.assertEqual(type(file.read()), str)
            self.assertEqual(rec1.to_dictionary(), json_dic1)
            self.assertEqual(rec2.to_dictionary(), json_dic2)

    def test_N_save_to_file(self):
        """
        testing the method save_to_file with a Square instance
        """
        squ1 = Square(10, 2, 8)
        squ2 = Square(2, 4)
        json_dic1 = {"id": 1, "size": 10, "y": 8, "x": 2}
        json_dic2 = {"y": 0, "id": 2, "x": 4, "size": 2}
        Square.save_to_file([squ1, squ2])
        with open("Square.json", 'r') as file:
            self.assertEqual(type(file.read()), str)
            self.assertEqual(squ1.to_dictionary(), json_dic1)
            self.assertEqual(squ2.to_dictionary(), json_dic2)

    def test_O_save_to_file(self):
        """
        Testing save_to_file empty
        """
        Base.save_to_file([])
        with open("Base.json", 'r') as file:
            self.assertEqual('[]', file.read())

    def test_P_from_json_string(self):
        """
        testing empty from_json_string
        """
        self.assertEqual(Base.from_json_string(None), [])

    def test_Q_id_valid_isprivate(self):
        """
        Testing if __nb_objects is private
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_R_params_exceptions_args_six(self):
        """
        Testing wrong number of arguments, six
        """
        with self.assertRaises(TypeError):
            r = Base(2, 3, 23, 12, 234, 4)

    def tearDown(self):
        """ Resset module for id """

        Base._Base__nb_objects = 0
