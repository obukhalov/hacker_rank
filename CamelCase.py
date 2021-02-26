#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    _counter = 0
    for i in range(len(s)):
        if s[i].isupper():
            _counter += 1

    return _counter + 1


if __name__ == '__main__':

    s = input()

    result = camelcase(s)

    print(str(result) + '\n')
