#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = matrix[:]
    for i in range(len(newmatrix)):
        for j in range(len(newmatrix[i])):
            newmatrix[i][j] = newmatrix[i][j]**2

    return newmatrix
