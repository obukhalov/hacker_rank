#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the marsExploration function below.
def marsExploration(s):
    _exp = 'SOS' * (len(s) // 3)
    _diff = 0

    for i in range(len(s)):
        if s[i] != _exp[i]:
            _diff += 1

    return _diff


if __name__ == '__main__':

    s = input()

    result = marsExploration(s)

    print(str(result) + '\n')
