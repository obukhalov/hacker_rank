#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    _result = []

    for _ in range(k):
        _n = a.pop()
        a.insert(0,_n)

    for _i in queries:
        _result.append(a[_i])

    return _result


if __name__ == '__main__':

    nkq = input().split()

    n = int(nkq[0])

    k = int(nkq[1])

    q = int(nkq[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    print('\n'.join(map(str, result)))
    print('\n')
