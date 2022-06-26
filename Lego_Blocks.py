#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def legoBlocks(n, m):
    # Write your code here

    MOD = 1000000007
    combinations = [1, 1, 2, 4]
    total = [1, 1, 2 ** n, 4 ** n]

    while len(combinations) <= m:
        c = sum(combinations[-4:]) % MOD
        combinations.append(c)  # possible combinations for one row
        total.append(pow(c, n, MOD))  # possible combinations for 'n' rows

    stable = [0, 1]

    for i in range(2, m + 1):
        stable.append(
            total[i] - sum((stable[j] * total[i - j]) for j in range(1, i)) % MOD
        )

    return stable[m] % MOD


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        print(str(result) + "\n")
