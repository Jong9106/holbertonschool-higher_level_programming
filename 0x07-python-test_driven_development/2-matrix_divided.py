#!/usr/bin/python3
""" Function to divide a matrix by given number """


def matrix_divided(matrix, div):
    """
    Function to divide a matrix by given number and return
    and raise some errors for edge cases
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list:
        raise TypeError(error)
    if len(matrix) == 0:
        raise TypeError(error)
    for y in range(len(matrix)):
        if type(matrix[y]) is not list:
            raise TypeError(error)
        if len(matrix[y]) == 0:
            raise TypeError(error)
        if len(matrix[0]) != len(matrix[y]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in range(len(matrix[y])):
            if type(matrix[y][x]) is None:
                raise TypeError(error)
            if type(matrix[y][x]) not in (int, float):
                raise TypeError(error)

    return [[round(x[i]/div, 2) for i in range(len(x))]for x in matrix]
