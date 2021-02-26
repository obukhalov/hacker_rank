#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    _chg = True
    _s1 = s
    while _chg:
        _chg = False
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                _s1 = s[:i] + s[i+2:]
                _chg = True
        s = _s1

    if s == '':
        return 'Empty String'
    else:
        return s

if __name__ == '__main__':

    s = input()

    result = superReducedString(s)

    print(result + '\n')
