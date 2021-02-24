#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the countingSort function below.
def countingSort(arr):
    _res_idx = [0 for _ in range(100)]
    for _n in arr:
        _res_idx[_n] += 1

    _res_lst = []
    for i in range(len(_res_idx)):
        if _res_idx[i] != 0:
            _res_lst.extend([i for _ in range(_res_idx[i])])


    return _res_lst

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    print(' '.join(map(str, result)))
    print('\n')
