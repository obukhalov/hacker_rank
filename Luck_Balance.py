#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(reverse=True)
    _res = 0
    for _c in contests:
        if _c[1] == 0:
            _res += _c[0]
        else:
            if k == 0:
                _res -= _c[0]
            else:
                _res += _c[0]
                k -= 1

    return _res

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    print(str(result) + '\n')
