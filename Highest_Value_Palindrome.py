#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    # Write your code here

    # For simplicity we will work with list of numbers instead of string
    ls = [ int(i) for i in s ] 

    # Find all the differences which prevent string to be polyndrome
    chg = 0
    for i in range(n//2):
        if ls[i] != ls[(i + 1) * -1]:
            chg += 1

    # If cganges more than k that it's not possible to create polyndrome
    if chg > k:
        return '-1'

    # Extra changes that could be done on string
    extra_chg = k - chg

    for i in range(n//2):
        if ls[i] == ls[(i + 1) * -1]:
            if ls[i] != 9 and extra_chg >= 2:
                ls[i] = 9
                ls[(i + 1) * -1] = 9
                extra_chg -= 2
        else:
            max_n = max(ls[i], ls[(i + 1) * -1])
            if max_n != 9 and extra_chg >= 1:
                ls[i] = 9
                ls[(i + 1) * -1] = 9
                extra_chg -= 1
            else:
                ls[i] = max_n
                ls[(i + 1) * -1] = max_n 

    if n % 2 == 1 and extra_chg > 0:
        ls[n // 2] = 9

    return ''.join([ str(i) for i in ls ])


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    print(result + '\n')
