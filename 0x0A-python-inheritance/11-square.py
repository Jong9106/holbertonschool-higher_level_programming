#!/usr/bin/python3
""" Module to define a new class """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ New Class Square that inherits from Rectangle """

    def __init__(self, size):
        self.__size = size

        self.integer_validator('size', size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))
