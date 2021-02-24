#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    _res = [0 for _ in range(100)]
    for _n in arr:
        _res[_n] += 1

    return _res

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
    print('\n')
