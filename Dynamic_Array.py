#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#


def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    answers_list = []
    arr = []
    for i in range(n):
        arr.append([])
    for q in queries:
        if q[0] == 1:
            idx = (q[1] ^ lastAnswer) % n
            arr[idx].append(q[2])
        elif q[0] == 2:
            idx = (q[1] ^ lastAnswer) % n
            lastAnswer = arr[idx][q[2] % len(arr[idx])]
            answers_list.append(lastAnswer)
    return answers_list


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print("\n".join(map(str, result)))
    print("\n")
