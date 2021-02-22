#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the runningTime function below.
def runningTime(arr):
    
    _swap = 0
    for i in range(1,len(arr)):
        print('i={}'.format(i))
        print('arr before: {}'.format(arr))
        _i2 = i
        _i1 = i 
        for j in range(i-1,-1,-1):
            if arr[j] <= arr[i]:
                break
            else:
                _i1 = j

        if _i1 == _i2:
            print('arr after: {}\tswap: {}'.format(arr,0))
        else:
            _n = arr.pop(_i2)
            arr.insert(_i1, _n)
            _swap += _i2 - _i1
            print('arr after: {}\tswap: {}'.format(arr,_i2 - _i1))

    return _swap
    

if __name__ == '__main__':

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    print(str(result) + '\n')
