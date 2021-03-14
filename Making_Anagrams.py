#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the makingAnagrams function below.
def makingAnagrams(s1, s2):
    _s1_s = set(s1)
    _s2_s = set(s2)

    _intersect_s = _s1_s.intersection(_s2_s)
    _counter = 0
    for _s in s1:
        if _s not in _intersect_s:
            _counter += 1
    for _s in s2:
        if _s not in _intersect_s:
            _counter += 1
    for _s in _intersect_s:
        _counter += abs(s1.count(_s) - s2.count(_s))

    return _counter


if __name__ == '__main__':

    s1 = input()

    s2 = input()

    result = makingAnagrams(s1, s2)

    print(str(result) + '\n')
