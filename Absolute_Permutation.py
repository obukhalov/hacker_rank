#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the absolutePermutation function below.
def absolutePermutation(n, k):
    _combs = []
    if k == 0:
        return [i for i in range(1,n+1)]
    elif n % (k * 2) != 0:
        return [-1]

    i = 1
    while i <= n:
        for j in range(k):
            _combs.append(i+k)
            i += 1
        for j in range(k):
            _combs.append(i-k)
            i += 1

    return _combs
            
                


if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        result = absolutePermutation(n, k)

        print(' '.join(map(str, result)))
