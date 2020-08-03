#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):

    _hits = 0
    while len(ar) >= 2:
        _first = ar.pop(0)
        for i in range(len(ar)):
            if (_first + ar[i]) % k == 0:
                _hits += 1

    return _hits


if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    print(str(result) + '\n')
