#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the countSort function below.
def countSort(arr):
    for i in range(len(arr) // 2):
        arr[i][1] = '-'

    arr.sort(key=lambda x:int(x[0]))

    for _e in arr:
        print(_e[1], end=' ')


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
