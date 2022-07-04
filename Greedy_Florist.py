#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    # Sort c in reverse order
    c.sort(reverse=True)

    # List with purchase counts of each friend
    pc = [0] * k

    # Index in pc list
    i = 0
    msum = 0

    for fc in c:
        msum += (pc[i] + 1) * fc
        pc[i] += 1
        i += 1
        if i == k:
            i = 0

    return msum


if __name__ == "__main__":

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    print(str(minimumCost) + "\n")
