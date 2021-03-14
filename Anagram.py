#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the anagram function below.
def anagram(s):
    if len(s) % 2 != 0:
        return -1
    _l = len(s) // 2
    _first = s[:_l]
    _second = s[_l:]
    _first_s = set(_first)
    _second_s = set(_second)
    _first_d = {}
    _second_d = {}
    for _s in _first_s:
        _first_d[_s] = _first.count(_s)
    for _s in _second_s:
        _second_d[_s] = _second.count(_s)

    _count = 0
    for _k in _first_d:
        if _k in _second_d.keys():
            if _first_d[_k] > _second_d[_k]:
                _count += _first_d[_k] - _second_d[_k]
        else:
            _count += _first_d[_k]


    return _count 


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(str(result) + '\n')
