#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c, k):
    _e = 100

    if k == len(c):
        if c[0] == 1:
            _e -= 3
        else:
            _e -= 1

        return _e

    i = k
    if c[i] == 1:
        _e -= 3
    else:
        _e -= 1

    while i != 0:
        if i + k >= len(c):
            i = abs(len(c) - (i + k))
        else:
            i += k

        if c[i] == 1:
            _e -= 3
        else:
            _e -= 1

    return _e 


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

    print(str(result) + '\n')
