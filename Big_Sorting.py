#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
def bigSorting(unsorted):
    _sorted = []
    _dict = {}
    for _n in unsorted:
        _len_n = len(_n)
        if _dict.get(_len_n):
            _dict[_len_n].append(_n)
        else:
            _dict[_len_n] = []
            _dict[_len_n].append(_n)

    for _key in sorted(list(_dict.keys())):
        if len(_dict[_key]) == 1:
            _sorted.append(_dict[_key][0])
        else:
            _lst = _dict[_key]
            _lst.sort(key=lambda i: int(i))
            _sorted.extend(_lst)


    return _sorted

if __name__ == '__main__':

    n = int(input())

    unsorted = []

    for _ in range(n):
        unsorted_item = input()
        unsorted.append(unsorted_item)

    result = bigSorting(unsorted)

    print('\n'.join(result))

