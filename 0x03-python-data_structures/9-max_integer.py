#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        hg = my_list[0]
        for i in my_list:
            if i > hg:
                hg = i
        return hg
    return None
