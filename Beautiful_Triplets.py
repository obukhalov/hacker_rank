#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the beautifulTriplets function below.
def beautifulTriplets(d, arr):
    _count = 0
    for i in range(len(arr)):
        _start = arr[i]
        if _start in arr and (_start + d) in arr and (_start + 2*d) in arr:
            _count += 1

    return _count 
    

if __name__ == '__main__':

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    print(str(result) + '\n')
