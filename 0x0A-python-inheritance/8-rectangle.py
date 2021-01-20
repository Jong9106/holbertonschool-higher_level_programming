#!/usr/bin/python3
""" Module to define a new class """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ New Class Rectangle that inherits from BaseGeometry """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        self.integer_validator('width', width)
        self.integer_validator('height', height)
