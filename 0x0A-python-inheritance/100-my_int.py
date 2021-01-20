#!/usr/bin/python3
""" Module to define a new class """


class MyInt(int):
    """ A class MyInt that inherits from int """
    
    def __eq__(self, op):
        return self.real != op

    def __ne__(self, op):
        return self.real == op
