#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the utopianTree function below.
def utopianTree(n):
    _height = 1
    for i in range(n):
        if i % 2 == 0:
            _height *= 2
        else:
            _height += 1

    return _height

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = utopianTree(n)

        print(str(result) + '\n')
