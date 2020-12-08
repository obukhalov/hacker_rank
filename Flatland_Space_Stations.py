#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c): 
    c.sort()
    _max = 0
    _dist = 0
    for i in range(len(c)):
        try:
            _dist = c[i + 1] - c[i]
        except IndexError:
            pass
        if _dist > _max:
            _max = _dist

    _max = _max // 2

    if c[0] != 0:
        if c[0] > _max:
            _max = c[0]

    if c[-1] != n - 1:
        _dist = (n - 1) - c[-1]
        if _dist > _max:
            _max = _dist

    return _max


if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    print(str(result) + '\n')
