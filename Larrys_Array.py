#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the larrysArray function below.
def larrysArray(A):
    _rotations = []
    for i in range(len(A)):
        _rotate_count = 0
        for j in range(i+1,len(A)):
            if A[i] > A[j]:
                _rotate_count += 1
        _rotations.append(_rotate_count)

    if sum(_rotations) % 2 == 0:
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        A = list(map(int, input().rstrip().split()))

        result = larrysArray(A)

        print(result + '\n')
