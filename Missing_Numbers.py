#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    _d_arr = {}
    _d_brr = {}
    for _e in arr:
        if _d_arr.get(_e):
            _d_arr[_e] += 1
        else:
            _d_arr[_e] = 1
    for _e in brr:
        if _d_brr.get(_e):
            _d_brr[_e] += 1
        else:
            _d_brr[_e] = 1

    _res = []
    for _k in _d_brr:
        if _d_arr.get(_k):
            if _d_brr[_k] > _d_arr[_k]:
                _res.append(_k)
        else:
            _res.append(_k)

    _res.sort()

    return _res


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(' '.join(map(str, result)))
    print('\n')
