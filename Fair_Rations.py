#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the fairRations function below.
def fairRations(B):
    _count = 0
    if sum(B) % 2 == 1:
        return 'NO'

    while 1 in [ i % 2 for i in B ]:
        for i in range(len(B)):
            if B[i] % 2 == 1:
                B[i] = B[i] + 1
                B[i+1] = B[i+1] + 1
                _count += 2


    return _count

if __name__ == '__main__':

    N = int(input())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    print(str(result) + '\n')
