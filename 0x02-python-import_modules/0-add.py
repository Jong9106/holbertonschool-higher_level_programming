#!/usr/bin/python3
if __name__ == "__main__":
    # desde el archivo/funcion/alias
    from add_0 import add as suma
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, suma(a, b)))
