#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    s = s.lower()
    s = s.replace(" ", "")
    if len(set(s)) == 26:
        return 'pangram'
    else:
        return 'not pangram'

if __name__ == '__main__':

    s = input()

    result = pangrams(s)

    print(result + '\n')

