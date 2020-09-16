#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    if len(s) >= n:
        return s[:n].count('a')
    else:
        _n_whole_s = n // len(s)
        _remain = n % len(s)
        return (s.count('a') * _n_whole_s) + s[:_remain].count('a')

if __name__ == '__main__':

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    print(str(result) + '\n')
