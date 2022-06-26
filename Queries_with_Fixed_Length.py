#!/bin/python3

import math
import os
import random
import re
import sys
import queue

#
# Complete the 'solve' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY queries
#


def solve(arr, queries):
    # Write your code here
    result = []
    n = len(arr)

    for d in queries:
        rmin = rmax = max(arr[:d])

        for i in range(1, n - d + 1):
            if arr[i - 1] == rmax:
                rmax = max(arr[i : i + d])
                if rmax < rmin:
                    rmin = rmax
        result.append(rmin)

    return result


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = solve(arr, queries)

    print("\n".join(map(str, result)))
