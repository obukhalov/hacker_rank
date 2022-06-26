#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    square_size = len(arr)
    left_to_right = sum([arr[i][i] for i in range(square_size)])
    right_to_left = sum([arr[i][(i + 1) * -1] for i in range(square_size)])

    return abs(left_to_right - right_to_left)

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(str(result) + '\n')
