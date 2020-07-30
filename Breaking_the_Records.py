#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    _min = scores[0]
    _max = scores[0]
    _high = 0
    _low = 0
    for _s in scores:
        if _s < _min:
            _low += 1
            _min = _s
        elif _s > _max:
            _high += 1
            _max = _s

    return [_high, _low]


if __name__ == '__main__':

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    print(' '.join(map(str, result)))
    print('\n')
