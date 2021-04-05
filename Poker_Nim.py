#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the pokerNim function below.
def pokerNim(k, c):
    _count = 0
    for _n in c:
        _count ^= _n


    if _count:
        return 'First'
    else:
        return 'Second'

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        c = list(map(int, input().rstrip().split()))

        result = pokerNim(k, c)

        print(result + '\n')
