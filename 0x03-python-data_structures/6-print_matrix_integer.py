#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    '''
        prints a matrix of integers.
    '''
    if matrix:
        for i in range(len(matrix)):
            for n in range(len(matrix[i])):
                if n == len(matrix[i]) - 1:
                    print("{:d}".format(matrix[i][n]))
                else:
                    print("{:d}".format(matrix[i][n]), end=" ")
    if len(matrix[0]) == 0:
        print("")
