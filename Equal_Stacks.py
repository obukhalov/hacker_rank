#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#


def equalStacks(h1, h2, h3):
    # Write your code here

    sum_h1 = []
    summary = 0

    for i in range(len(h1) - 1, -1, -1):
        summary += h1[i]
        sum_h1.append(summary)

    sum_h2 = []
    summary = 0

    for i in range(len(h2) - 1, -1, -1):
        summary += h2[i]
        sum_h2.append(summary)

    sum_h3 = []
    summary = 0

    for i in range(len(h3) - 1, -1, -1):
        summary += h3[i]
        sum_h3.append(summary)

    set_h1 = set(sum_h1)
    set_h2 = set(sum_h2)
    set_h3 = set(sum_h3)

    set_intersect = set_h1.intersection(set_h2)
    set_intersect.intersection_update(set_h3)

    if len(set_intersect) == 0:
        return 0
    else:
        return max(set_intersect)


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(str(result) + "\n")
