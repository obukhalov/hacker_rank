#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):
    _num_names = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'quarter',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    21 : 'twenty one',
    22 : 'twenty two',
    23 : 'twenty three',
    24 : 'twenty four',
    25 : 'twenty five',
    26 : 'twenty six',
    27 : 'twenty seven',
    28 : 'twenty eight',
    29 : 'twenty nine',
    30 : 'half'
    }

    if m == 0:
        return _num_names[h] + " o' clock"
    elif m == 1:
        return _num_names[m] + ' minute past ' + _num_names[h]
    elif m == 59:
        return _num_names[m] + ' minute to ' + _num_names[h]
    elif m == 15:
        return _num_names[m] + ' past ' + _num_names[h]
    elif m == 45:
        return _num_names[60 - m] + ' to ' + _num_names[h + 1]
    elif m < 30:
        return _num_names[m] + ' minutes past ' + _num_names[h]
    elif m == 30:
        return _num_names[m] + ' past ' + _num_names[h]
    elif m > 30:
        return _num_names[60 - m] + ' minutes to ' + _num_names[h + 1]


if __name__ == '__main__':

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    print(result + '\n')
