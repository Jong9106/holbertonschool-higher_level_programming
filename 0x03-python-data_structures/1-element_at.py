#!/usr/bin/python3
def element_at(my_list, idx):
    cont = len(my_list)
    if idx < 0 and cont < idx:
        return None
    for str in range(cont):
        if str == idx:
            return my_list[idx]:
