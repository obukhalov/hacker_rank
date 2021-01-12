#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(t):
    _lower = 1
    _mid = 3
    _upper = 3
    while t > _upper:
        _lower = _upper + 1
        _upper = _upper + 2 * _mid
        _mid = 2 * _mid

    return _mid - (t - _lower )



if __name__ == '__main__':

    t = int(input())

    result = strangeCounter(t)

    print(str(result) + '\n')
