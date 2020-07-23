#!/usr/bin/env python

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if 'PM' in s:
        if int(s[:2]) == 12:
            return '12' + s[2:-2]
        else:
            return str(int(s[:2]) + 12) + s[2:-2]
    else:
        if int(s[:2]) == 12:
            return '00' + s[2:-2]
        else:
            return s[:-2] 

if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')

