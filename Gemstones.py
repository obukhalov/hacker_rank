#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the gemstones function below.
def gemstones(arr):
    _l = len(arr)
    _gem = set()
    for _s in arr[0]:
        if len([_str for _str in arr if _s in _str]) == _l:
            _gem.add(_s)
            #print('Symbol: {}'.format(_s))

    return len(_gem)


if __name__ == '__main__':

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = input()
        arr.append(arr_item)

    result = gemstones(arr)

    print(str(result) + '\n')
