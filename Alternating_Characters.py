#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(s):
    _str_lst = [s[0]]
    for i in range(1,len(s)):
        if s[i] == _str_lst[-1][-1]:
            _str_lst[-1] += s[i]
        else:
            _str_lst.append(s[i])

    _count = 0
    for _g in _str_lst:
        if _g != 1:
            _count += len(_g) - 1

    return _count

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        print(str(result) + '\n')
