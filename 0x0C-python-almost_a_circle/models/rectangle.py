#!/usr/bin/python3
""" Module to create a new class """

from models.base import Base

class Rectangle(Base):
    """ New class Rectangle that inheriths from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.height = height
        
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.x = x

        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.y = y

        @property
        def width(self):
            return self.width

        @width.setter
        def width(self, value):
            if type(value) is not int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")

        @property
        def height(self):
            return self.height

        @height.setter
        def height(self, value):
            if type(value) is not int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")

        @property
        def x(self):
            return self.x

        @x.setter
        def x(self, value):
            if type(value) is not int:
                raise TypeError("x must be an integer")
            if value <= 0:
                raise ValueError("x must be > 0")

        @property
        def y(self):
            return self.y

        @width.setter
        def y(self, value):
            if type(value) is not int:
                raise TypeError("y must be an integer")
            if value <= 0:
                raise ValueError("y must be > 0")