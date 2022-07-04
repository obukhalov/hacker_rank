#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countLuck' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY matrix
#  2. INTEGER k
#


def countLuck(matrix, k):
    # Write your code here

    # Convert every element of matrix into list object to make it mutable
    matrix = [list(line) for line in matrix]

    # Define n and m values
    n = len(matrix)
    m = len(matrix[0])

    # Find the start point
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "M":
                start = [i, j]

    # Find the finish point
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "*":
                finish = [i, j]

    # Change direction counter
    k1 = 0

    # Count change directions
    step = start
    path = []

    while step != finish:
        i, j = step[0], step[1]

        dr = []

        if matrix[i][j] == "0":
            step = path.pop()
        else:
            nbrs = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]

            for i1, j1 in nbrs:
                if (0 <= i1 <= n - 1) and (0 <= j1 <= m - 1):
                    if matrix[i1][j1] == "." or matrix[i1][j1] == "*":
                        dr.append([i1, j1])

            if len(dr) == 0:
                if matrix[i][j] == ".":
                    matrix[i][j] = "0"
                step = path.pop()
            else:
                if matrix[i][j] == "." or matrix[i][j] == "M" or matrix[i][j] == "1":
                    path.append([i, j])
                if matrix[i][j] == "." and len(dr) == 1:
                    matrix[i][j] = "0"
                if matrix[i][j] == "M" and len(dr) == 1:
                    matrix[i][j] = "0"
                if matrix[i][j] == "." and len(dr) > 1:
                    matrix[i][j] = "1"
                if matrix[i][j] == "M" and len(dr) > 1:
                    matrix[i][j] = "1"
                step = dr.pop()

    for i, j in path:
        if matrix[i][j] == "1":
            k1 += 1

    if k == k1:
        return "Impressed"
    else:
        return "Oops!"


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        matrix = []

        for _ in range(n):
            matrix_item = input()
            matrix.append(matrix_item)

        k = int(input().strip())

        result = countLuck(matrix, k)

        print(result + "\n")
