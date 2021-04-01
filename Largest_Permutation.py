#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, arr):
    n = len(arr)
    if k >= n:
        return [i for i in range(n,0,-1)]
    _high = [i for i in range(n,0,-1)]
    i = 0
    while k > 0 and i <= (n - 1):
        if arr[i] == _high[i]:
            i += 1
            continue
        else:
            _sw_idx = arr.index(_high[i])
            _sw_el = arr[i]
            arr[i] = _high[i]
            arr[_sw_idx] = _sw_el
            k -= 1
            i += 1

    return arr





if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))

    result = largestPermutation(k, arr)

    print(' '.join(map(str, result)))
    print('\n')
