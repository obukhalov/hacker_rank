#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def lilysHomework(arr):
    # Write your code here
    n = len(arr)

    # Dictionary for elements lookup. Key is element in sorted source array, value is it's index in source array
    forward_d = {e: i for i, e in enumerate(sorted(arr))}
    reverse_d = {e: i for i, e in enumerate(sorted(arr, reverse=True))}

    # Find counter in sorted array
    counter_f = 0
    arr_c = arr.copy()
    i1 = 0
    while i1 < n:
        i2 = forward_d[arr_c[i1]]
        if i1 == i2:
            i1 += 1
            continue
        arr_c[i1], arr_c[i2] = arr_c[i2], arr_c[i1]
        counter_f += 1

    # Find counter in reverse sorted array
    counter_r = 0
    arr_c = arr.copy()
    i1 = 0
    while i1 < n:
        i2 = reverse_d[arr_c[i1]]
        if i1 == i2:
            i1 += 1
            continue
        arr_c[i1], arr_c[i2] = arr_c[i2], arr_c[i1]
        counter_r += 1

    return min(counter_f, counter_r)


if __name__ == "__main__":

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    print(str(result) + "\n")
