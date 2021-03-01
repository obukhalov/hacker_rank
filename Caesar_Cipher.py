#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the caesarCipher function below.
def caesarCipher(s, k):
    _alphabet = 'abcdefghijklmnopqrstuvwxyz'
    _encr_s = ''
    if k > 26:
        k = k % 26
    for _s in s:
        if _s.isalpha():
            if _s.isupper():
                _clear_idx = _alphabet.index(_s.lower())
                if _clear_idx + k > 25:
                    _encr_idx = _clear_idx + k - 26
                else:
                    _encr_idx = _clear_idx + k
                _encr_s += _alphabet[_encr_idx].upper()
            else:
                _clear_idx = _alphabet.index(_s)
                if _clear_idx + k > 25:
                    _encr_idx = _clear_idx + k - 26
                else:
                    _encr_idx = _clear_idx + k
                _encr_s += _alphabet[_encr_idx]
        else:
            _encr_s += _s

    return _encr_s



if __name__ == '__main__':

    n = int(input())

    s = input()

    k = int(input())

    result = caesarCipher(s, k)

    print(result + '\n')
