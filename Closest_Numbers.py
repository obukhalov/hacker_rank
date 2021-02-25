#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr.sort()
    _diff_lst = []
    for i in range(len(arr)-1):
        _diff_lst.append(abs(arr[i]-arr[i+1]))

    _min_diff = min(_diff_lst)
    _res_arr = []
    for i in range(len(_diff_lst)):
        if _diff_lst[i] == _min_diff:
            _res_arr.append(arr[i])
            _res_arr.append(arr[i+1])

    return _res_arr

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    print(' '.join(map(str, result)))
    print('\n')
