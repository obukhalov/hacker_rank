#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    _count = 0
    _p = 1
    for _ch in arr:
        _low = 0
        _high = 0
        while _ch > _low:
            if _low + k <= _ch:
                _high = _low + k
            else:
                _high = _ch

            print('Chapter: {} - Low: {} High: {} Page {}'.format(_ch, _low, _high, _p))
            if _p >= _low + 1 and _p <= _high:
                _count += 1
                print('Count: {}'.format(_count))
            _low = _high
            _p += 1

    return _count



if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    print(str(result) + '\n')
