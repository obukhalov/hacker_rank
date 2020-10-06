#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):

    result = []
    for _n in range(p,q+1):
        _right = int(str(_n ** 2)[len(str(_n)) * -1:])
        _left_s = str(_n ** 2)[:len(str(_n)) * -1]
        if _left_s == '':
            _left = 0
        else:
            _left = int(_left_s)

        if _n == _left + _right:
            result.append(str(_n))

    if result:
        print(' '.join(result))
    else:
        print('INVALID RANGE')

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
