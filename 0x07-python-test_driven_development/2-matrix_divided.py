#!/usr/bin/python3
""" Function to divide a matrix by given number """


def matrix_divided(matrix, div):
    """ commit """

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")


    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for y in range(len(matrix)):
        if type(matrix[y]) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[y]) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(matrix[0]) != len(matrix[y]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in range(len(matrix[y])):
            if type(matrix[y][x]) == None:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if type(matrix[y][x]) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    return [[round(x[i]/div, 2) for i in range(len(x))]for x in matrix]
