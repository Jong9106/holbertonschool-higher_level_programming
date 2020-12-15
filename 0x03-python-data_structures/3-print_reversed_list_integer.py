#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        cont = len(my_list)
        if cont:
            for str in my_list[::-1]:
                print("{:d}".format(str))
