#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    _grouping = {}
    while len(a) >0:
        _tmp_lst = [ a[i] for i in range(len(a)) if a[i] == a[0]]
        a = [ a[i] for i in range(len(a)) if a[i] != a[0]]
        _grouping[_tmp_lst[0]] = len(_tmp_lst)
    _lenght = []

    print(_grouping)
    if len(_grouping) == 1:
        _lenght.append(_grouping[list(_grouping.keys())[0]])
    else:
        for i in list(_grouping.keys()):
            _lenght.append(_grouping[i])
            for j in list(_grouping.keys()):
                if abs(i - j) != 0 and abs(i - j) <= 1:
                    _lenght.append(_grouping[i] + _grouping[j])

    return max(_lenght)


if __name__ == '__main__':

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')
