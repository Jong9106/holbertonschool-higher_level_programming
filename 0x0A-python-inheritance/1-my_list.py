#!/usr/bin/python3
""" Define a MyList class """


class MyList(list):
    """ Class Mylist and print it self sorted """

    def print_sorted(self):
        """ Function to print sorted elements """
        print(sorted(self))
