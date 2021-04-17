#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the misereNim function below.
def misereNim(s):
    if len(s) == sum(s):
        if len(s) % 2 == 1:
            return 'Second'
        else:
            return 'First'
    _res = 0
    for _e in s:
        _res ^= _e
    if _res:
        return 'First'
    else:
        return 'Second'

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        print(result + '\n')
