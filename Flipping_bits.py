#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the flippingBits function below.
def flippingBits(n):
    _bin_n = bin(n)[2:]
    _32_bit_bin = '0'*(32-len(_bin_n)) + _bin_n
    _inverted_32_bit_bin = ''
    for _b in _32_bit_bin:
        if _b == '0':
            _inverted_32_bit_bin += '1'
        elif _b == '1':
            _inverted_32_bit_bin += '0'


    return int(_inverted_32_bit_bin, base=2)


if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        result = flippingBits(n)

        print(str(result) + '\n')
