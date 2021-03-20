#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the icecreamParlor function below.
def icecreamParlor(m, arr):
    for i in range(len(arr)):
        if arr[i] < m:
            _f1 = arr[i] 
            _f2 = m - _f1
            try:
                i2 = arr[i+1:].index(_f2)
            except ValueError:
                continue

            return sorted([i+1,(i+1)+(i2+1)])

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        m = int(input())

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        print(' '.join(map(str, result)))
        print('\n')
