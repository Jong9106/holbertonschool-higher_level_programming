#!/usr/bin/python3
def uppercase(str):
    for l in str:
        n = ord(l)
        if n >= 97 and n <= 122:
            n -= 32
        print("{:c}".format(n), end="")
    print()
