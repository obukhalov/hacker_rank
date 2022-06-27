#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour, minutes, seconds = s[:-2].split(':')
    if s[-2:] == 'AM':
        if hour == '12':
            hour = '00'
        return f'{hour}:{minutes}:{seconds}'
    else:
        if hour != '12':
            hour = str(int(hour) + 12)
        return f'{hour}:{minutes}:{seconds}'


if __name__ == '__main__':

    s = input()

    result = timeConversion(s)

    print(result + '\n')
