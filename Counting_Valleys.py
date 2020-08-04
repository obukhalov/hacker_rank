#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    _valleys = 0
    _path = 0
    for i in range(n):
        if s[i] == 'D':
            _path -= 1
        elif s[i] == 'U':
            if _path < 0 and (_path + 1) == 0:
                _valleys += 1
            _path += 1
        #print('Valleys: {}\tPath: {}'.format(_valleys, _path))

    return _valleys


if __name__ == '__main__':

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    print(str(result) + '\n')
