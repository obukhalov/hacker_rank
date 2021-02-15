#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    for i in range(1,len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                _n = arr.pop(i)
                arr.insert(j,_n)
        print(' '.join(list(map(str,arr))))
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
