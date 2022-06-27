#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def maxSubarray(arr):
    # Write your code here

    positive_numbers = list(filter(lambda x: x > 0, arr))

    if len(positive_numbers) != 0:
        subseq_max_sum = sum(positive_numbers)
    else:
        return [max(arr), max(arr)]

    sum_set = set()

    summary = 0
    for n in arr:
        summary += n
        sum_set.add(summary)
        if summary < 0:
            summary = 0

    subarr_max_sum = max(sum_set)

    return [subarr_max_sum, subseq_max_sum]


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        print("\n")
        print(" ".join(map(str, result)))
        print("\n")
