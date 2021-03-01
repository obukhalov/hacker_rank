#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for _s in _alphabet:
        if not (_s in s or _s.upper() in s): 
            return 'not pangram'

    return 'pangram'


if __name__ == '__main__':

    s = input()

    result = pangrams(s)

    print(result + '\n')
