#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    _l = len(s)

    if _l % 2 == 0:
        _s_set = set(s)
        for _s in _s_set:
            if s.count(_s) % 2 == 1:
                return 'NO'
        return 'YES'
    else:
        _s_set = set(s)
        _odd = 0
        for _s in _s_set:
            if s.count(_s) % 2 == 1 and _odd >= 1:
                return 'NO'
            if s.count(_s) % 2 == 1:
                _odd += 1
        return 'YES'


if __name__ == '__main__':

    s = input()

    result = gameOfThrones(s)

    print(result + '\n')
