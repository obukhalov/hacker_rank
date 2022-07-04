#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#
def sub_sum(terms, X, comb, part=[]):
    s = sum(part)

    if s == X:
        return comb + 1
    if s > X:
        return comb

    for i in range(len(terms)):
        n = terms[i]
        remain = terms[i + 1 :]
        comb = sub_sum(remain, X, comb, part + [n])

    return comb


def powerSum(X, N):
    # Write your code here
    max_n = int(X ** (1 / N)) + 1
    terms = [i ** N for i in range(1, max_n + 1)]

    combs = sub_sum(terms, X, 0)

    return combs


if __name__ == "__main__":

    X = int(input().strip())

    N = int(input().strip())

    result = powerSum(X, N)

    print(str(result) + "\n")
