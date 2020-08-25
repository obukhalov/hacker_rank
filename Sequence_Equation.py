#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    _seq_dict = {}
    for i in range(len(p)):
        _seq_dict[p[i]] = i+1

    _res = []
    p.sort()
    for i in p:
        _res.append(_seq_dict[_seq_dict[i]])

    return _res


if __name__ == '__main__':

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    print('\n'.join(map(str, result)))
    print('\n')
