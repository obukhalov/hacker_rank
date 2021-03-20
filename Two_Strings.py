#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    s1_s = set(s1)
    s2_s = set(s2)

    if s1_s.intersection(s2_s):
        return 'YES'
    else:
        return 'NO'

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        print(result + '\n')
