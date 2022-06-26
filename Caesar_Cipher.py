#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if k > 26:
        k = k % 26
    chiper = alphabet[k:] + alphabet[:k]
    result = ""
    for l in s:
        if l.isalpha():
            idx = alphabet.index(l.lower())
            ch = chiper[idx]
            if l.isupper():
                result += ch.upper()
            else:
                result += ch
        else:
            result += l

    return result


if __name__ == "__main__":

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    print(result + "\n")
