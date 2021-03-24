#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    _min = abs(arr[0] - arr[1])
    for i in range(len(arr) - 1):
        _inter = abs(arr[i]-arr[i+1])
        if _inter < _min:
            _min = _inter


    return _min

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    print(str(result) + '\n')
