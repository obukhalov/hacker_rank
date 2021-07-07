#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the nimGame function below.
def nimGame(pile):
    _count = 0
    for _e in pile:
        _count ^= _e
    if _count:
        return 'First'
    else:
        return 'Second'

if __name__ == '__main__':

    g = int(input())

    for g_itr in range(g):
        n = int(input())

        pile = list(map(int, input().rstrip().split()))

        result = nimGame(pile)

        print(result + '\n')
