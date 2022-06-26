#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#


def icecreamParlor(m, arr):
    # Write your code here
    arr_with_idx = list(enumerate(arr, start=1))
    arr_with_idx_sotred = sorted(arr_with_idx, key=lambda x: x[1])

    while True:
        idx_c1, c1 = arr_with_idx_sotred.pop()

        if c1 < m:
            i = 0

            while arr_with_idx_sotred[i][1] <= m - c1:
                c2 = arr_with_idx_sotred[i][1]

                if c1 + c2 == m:
                    idx_c2 = arr_with_idx_sotred[i][0]
                    return sorted([idx_c2, idx_c1])
                else:
                    i += 1


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(" ".join(map(str, result)))
        print("\n")
