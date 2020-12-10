#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = number % 10
if number < 0:
    ld = number % -10
if ld > 5:
    str = "and is greater than 5"
    print("Last digit of {:d} is {:d} {:s}".format(number, ld, str))
elif ld == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, ld))
else:
    str = "and is less than 6 and not 0"
    print("Last digit of {:d} is {:d} {:s}".format(number, ld, str))
