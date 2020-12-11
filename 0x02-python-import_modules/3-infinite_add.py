#!/usr/bin/python3
if __name__ == "__main__":
    total = 0
    from sys import argv as av
    for i in av[1:]:
        total += int(i)
    print(total)
