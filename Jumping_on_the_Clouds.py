#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    _steps = 0
    _idx = 0
    while _idx < len(c) - 1:
        try:
            if c[_idx + 2] != 1:
                _idx += 2
                _steps += 1
                continue
        except IndexError:
            pass
        try:
            if c[_idx + 1] != 1:
                _idx += 1
                _steps += 1
                continue
        except IndexError:
            pass

    return _steps


if __name__ == '__main__':

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    print(str(result) + '\n')
