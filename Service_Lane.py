#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases):
    _min_lst = []
    for _case in cases:
        _min_lst.append(min(width[_case[0]:_case[1]+1]))
    return _min_lst

if __name__ == '__main__':

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    print('\n'.join(map(str, result)))
    print('\n')
