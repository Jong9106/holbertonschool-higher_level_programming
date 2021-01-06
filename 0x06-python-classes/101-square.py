#!/usr/bin/python3
"""Program to define atribute size"""


def __str__(self):
        """Returns string version of Square"""
        if self.size == 0:
            return ""
        sq = "\n" * self.position[1]
        for i in range(self.size):
            sq += "{}{}".format(" " * self.position[0], "#" * self.size)
            if i < self.size - 1:
                sq += "\n"
        return sq
