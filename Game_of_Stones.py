#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the gameOfStones function below.
def gameOfStones(n):
    if n % 7 == 0 or n % 7 == 1:
        return 'Second'
    else:
        return 'First'

if __name__ == '__main__':

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = gameOfStones(n)

        print(result + '\n')
