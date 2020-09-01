#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    _result_arr = []
    while len(arr) > 0:
        _result_arr.append(len(arr))
        _min = min(arr)
        arr = [ i for i in arr if i > _min ]

    return _result_arr


if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    print('\n'.join(map(str, result)))
    print('\n')
