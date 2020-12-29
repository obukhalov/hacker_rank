#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the stones function below.
def stones(n, a, b):
    _last_stone_num = set()
    _count_a = n - 1
    _count_b = 0
    for i in range(n):
        _stone_num = _count_a * a + _count_b * b
        _last_stone_num.add(_stone_num)
        _count_a -= 1
        _count_b += 1

    return sorted(_last_stone_num)


if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())

        result = stones(n, a, b)

        print(' '.join(map(str, result)))
        print('\n')
