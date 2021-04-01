#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the toys function below.
def toys(w):
    w.sort()
    _count = 1
    _min = w[0]
    _max = _min + 4
    for i in range(len(w)):
        if w[i] >= _min and w[i] <= _max:
            pass
        else:
            _count += 1
            _min = w[i]
            _max = _min + 4

    return _count 

if __name__ == '__main__':

    n = int(input())

    w = list(map(int, input().rstrip().split()))

    result = toys(w)

    print(str(result) + '\n')
