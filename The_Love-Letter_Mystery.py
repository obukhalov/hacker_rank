#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    _l = len(s)
    _count = 0
    for i in range(_l // 2):
        j = (i+1)*-1
        _count += abs(ord(s[i]) - ord(s[j]))

    return _count

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        print(str(result) + '\n')
