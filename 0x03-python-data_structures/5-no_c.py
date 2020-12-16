#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        new_string = ""
        for str in my_string:
            if str == "C" or str == "c":
                continue
            new_string += str
        return new_string
        