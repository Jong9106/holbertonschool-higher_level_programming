#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv as av
    ac = len(av) - 1
    i = 1
    if ac != 0 and ac != 1:
        print("{:d} arguments:".format(ac))
        for str in av[1:]:
            print("{:d}: {}".format(i, str))
            i += 1
    elif ac == 1:
        print("{:d} argument:".format(ac))
        for str in av[1:]:
            print("{:d}: {}".format(i, str))
    else:
        print("{:d} arguments.".format(ac))
