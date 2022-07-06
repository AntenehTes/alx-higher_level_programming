#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrixv2 = matrix.copy()

    for x in range(len(matrix)):
        matrixv2[x] = list(map(lambda y: y**2, matrix[x]))
    return (matrixv2)
