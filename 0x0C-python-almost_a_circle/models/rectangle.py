#!/usr/bin/python3
""" Module to create a new class """

from models.base import Base

class Rectangle(Base):
    """ New class Rectangle that inheriths from Base class """

    def __init__(self, width, height, x=0, y=0, id=None):
    
        super().__init__(id)

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
