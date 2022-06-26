#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
def cookies(k, A):
    # Write your code here
    heapq.heapify(A)

    counter = 0
    len_A = len(A)

    while len_A > 1:
        if A[0] >= k:
            return counter

        l1 = heapq.heappop(A)
        l2 = heapq.heappop(A)
        len_A -= 2
        val = l1 + 2 * l2
        counter += 1

        if len_A == 0:
            if val < k:
                return -1
            else:
                return counter

        heapq.heappush(A, val)
        len_A += 1

    return -1


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    print(str(result) + "\n")
