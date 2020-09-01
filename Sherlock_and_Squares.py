#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the squares function below.
def squares(a, b):
    _sqrt_int = []

    i = int(math.sqrt(a))
    _sqrt = i * i

    while _sqrt <= b:
        _sqrt = i * i
        if _sqrt >= a and _sqrt <= b:
            _sqrt_int.append(_sqrt)
        i += 1


    return len(_sqrt_int)

if __name__ == '__main__':


    q = int(input())

    _results = []

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)
        _results.append(result)

    for i in _results:
        print(i)
