#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort1 function below.
def insertionSort1(n, arr):
    _reverse = arr.copy()
    _reverse.reverse()
    _last = _reverse[0]
    _flag = False
    for i in range(len(arr) - 1):
        if _last < _reverse[i+1]:
            _reverse[i] = _reverse[i+1]
            _stright = _reverse.copy()
            _stright.reverse()
            print(' '.join(list(map(str,_stright))))
        else:
            _reverse[i] = _last
            _stright = _reverse.copy()
            _stright.reverse()
            print(' '.join(list(map(str,_stright))))
            _flag = True
            break

    if not _flag:
        if _reverse[-1] > _last:
            _reverse[-1] = _last
            _stright = _reverse.copy()
            _stright.reverse()
            print(' '.join(list(map(str,_stright))))



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
