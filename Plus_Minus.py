#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    _p = len([n for n in arr if n > 0])
    _n = len([n for n in arr if n < 0])
    _z = len([n for n in arr if n == 0])
    print('{:.6f}'.format(_p / len(arr)))
    print('{:.6f}'.format(_n / len(arr)))
    print('{:.6f}'.format(_z / len(arr)))
    

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

