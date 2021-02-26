#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    _spec_symbols = '!@#$%^&*()-+'
    _min = 4
    _digit = False
    _lower = False
    _upper = False
    _special = False
    for _s in password:
        if _s.isdigit():
            _digit = True
        elif _s.islower():
            _lower = True
        elif _s.isupper():
            _upper = True
        elif _s in _spec_symbols:
            _special = True

    if _digit:
        _min -= 1
    if _lower:
        _min -= 1
    if _upper:
        _min -= 1
    if _special:
        _min -= 1

    if n >= 6-_min:
        return _min
    else:
        return 6 - n

if __name__ == '__main__':

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    print(str(answer) + '\n')
