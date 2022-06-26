#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#


def flippingMatrix(matrix):
    # Write your code here
    n = len(matrix) // 2
    result = 0
    for row in range(n):
        for col in range(n):
            result += max(
                [
                    matrix[row][col],
                    matrix[row][(col * -1) - 1],
                    matrix[(row * -1) - 1][col],
                    matrix[(row * -1) - 1][(col * -1) - 1],
                ]
            )
    return result


if __name__ == "__main__":
    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(str(result) + "\n")
