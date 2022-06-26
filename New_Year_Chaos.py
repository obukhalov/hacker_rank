#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    n = len(q)
    bribes = 0
    for i in range(n, 0, -1):
        q_idx = i - 1
        if q[q_idx] == i:
            q.pop(q_idx)
        elif q[q_idx - 1] == i:
            bribes += 1
            q.pop(q_idx - 1)
        elif q[q_idx - 2] == i:
            bribes += 2
            q.pop(q_idx - 2)
        else:
            print("Too chaotic")
            return

    print(bribes)


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
