#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    del_char = ""
    for x in str:
        if i == n:
            i += 1
            continue
        del_char += x
        i += 1
    return (del_char)