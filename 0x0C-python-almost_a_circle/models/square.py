#!/usr/bin/python3
""" Module to create a new class """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ New class Square that inheriths from Base class """

    def __init__(self, size, x=0, y=0, id=None):
        """ Attributes for Square class """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Magic string representation of a class """
        return ("[Square] ({:d}) {:d}/{:d} - {:d}".format
                (self.id, self.x, self.y, self.width))

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
