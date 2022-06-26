#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    # Write your code here
    arr.sort()
    diff = arr[-1] - arr[0]
    n = len(arr)
    for i in range(n - k + 1):
        diff_tmp = arr[i + k - 1] - arr[i]
        if diff_tmp < diff:
            diff = diff_tmp
    return diff


if __name__ == "__main__":

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    print(str(result) + "\n")
