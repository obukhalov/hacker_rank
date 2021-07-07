#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the nimbleGame function below.
def nimbleGame(s):
    _win = 0
    for i in range(1,len(s)):
        if s[i] % 2 == 1: 
            _win ^= i 

    if _win:
        return 'First'
    else:
        return 'Second'

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        s = list(map(int, input().rstrip().split()))

        result = nimbleGame(s)

        print(result + '\n')
