#!/usr/bin/env python

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the birthday function below.
def birthday(s, d, m):
    _hits = 0
    for i in range(len(s)):
        if len(s[i:i+m]) == m and sum(s[i:i+m]) == d:
            _hits += 1

    return _hits


if __name__ == '__main__':

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    print(str(result) + '\n')
