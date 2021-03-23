#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    _max = 0
    for i in range(l,r+1):
        for j in range(i,r+1):
            a = i
            b = j
            a ^= b
            if a > _max:
                _max = a

    return _max

if __name__ == '__main__':

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    print(str(result) + '\n')
