#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    _etalon = 'hackerrank'
    for _s in _etalon:
        if _s in s:
            _idx = s.index(_s)
            s = s[_idx+1:]
        else:
            return 'NO'

    return 'YES'

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        print(result + '\n')
