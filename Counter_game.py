#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def counterGame(n):
    # Write your code here
    turn = 1
    if n == 1:
        return "Richard"
    while n != 1:
        log_n = math.log2(n)
        if log_n == int(log_n):
            n = n // 2
            turn += 1
        else:
            n = n - int(math.pow(2, int(log_n)))
            turn += 1

    if turn % 2 == 0:
        return "Louise"
    else:
        return "Richard"


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        print(result + "\n")
