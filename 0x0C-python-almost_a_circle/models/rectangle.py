#!/usr/bin/python3
""" Module to create a new class """


from models.base import Base


class Rectangle(Base):
    """ New class Rectangle that inheriths from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Attributes for Rectangle class """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ Public method that define area"""
        return self.__width * self.__height

    def display(self):
        """ Public method that define display """
        for k in range(self.y):
            print()
        for i in range(self.height):
            for l in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print('#', end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format
                (self.id, self.x, self.y, self.width, self.height))
