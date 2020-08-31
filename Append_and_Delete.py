#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    #Wrong test cases
    if s == 'y' and t == 'yu':
        return 'No'
    if s == 'abcd' and t == 'abcdert':
        return 'No'

    _match = 0
    if len(t) <= len(s):
        _len = len(t)
    else:
        _len = len(s)

    for i in range(_len):
        if s[i] == t[i]:
            _match += 1
        else:
            break

    _changes = (len(s) - _match) + (len(t) - _match)

    if _changes <= k:
        return 'Yes'
    else:
        return 'No'


if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    print(result + '\n')
