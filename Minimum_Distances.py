#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    _max = len(a)
    _min = len(a)
    for i in range(len(a)):
        try:
            _d = a.index(a[i], i+1) - i
            if _d < _min:
                _min = _d
        except ValueError:
            pass

    if _min != _max:
        return _min
    else:
        return -1


if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    print(str(result) + '\n')
