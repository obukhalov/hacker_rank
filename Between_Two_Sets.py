#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def getTotalX(a, b):
    # Write your code here
    start = max(a)
    end = min(b)
    counter = 0
    for i in range(start, end + 1):
        if not any(map(lambda x: i % x, a)) and not any(map(lambda x: x % i, b)):
            counter += 1
    return counter


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    print(str(total) + "\n")
