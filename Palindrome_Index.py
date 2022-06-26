#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def ispalindrome(s):
    len_s = len(s) // 2
    for i in range(len_s):
        if s[i] != s[i * -1 - 1]:
            return False
    return True


def palindromeIndex(s):
    # Write your code here
    len_s = len(s)
    for i in range(len_s // 2):
        if s[i] != s[i * -1 - 1]:
            if ispalindrome(s[i + 1 : len_s - i]):
                return i
            elif ispalindrome(s[i : len_s - 1 - i]):
                return len_s - i - 1
    return -1


if __name__ == "__main__":

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(str(result) + "\n")
