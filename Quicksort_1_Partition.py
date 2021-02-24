#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the quickSort function below.
def quickSort(arr):
    _pivot = arr.pop(0)
    _res_left = [] 
    _res_right = [] 

    for _n in arr:
        if _n <= _pivot:
            _res_left.append(_n)
        else:
            _res_right.append(_n)

    return _res_left + [_pivot] + _res_right




if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    print(' '.join(map(str, result)))
    print('\n')
