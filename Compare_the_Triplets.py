#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    _a_score = 0
    _b_score = 0
    for i in range(3):
        if a[i] > b[i]:
            _a_score += 1
        elif a[i] < b[i]:
            _b_score += 1

    return (_a_score, _b_score)

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(' '.join(map(str, result)))

