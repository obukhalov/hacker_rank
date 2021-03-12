#!/usr/bin/env python

import math
import os
import random
import re
import sys

#Check if palindrome
def if_palindrome(s):
    _l = len(s)
    for i in range(_l // 2):
        if s[i] != s[_l-1-i]:
            return False
    return True

# Complete the palindromeIndex function below.
def palindromeIndex(s):
    _l = len(s)
    for i in range(_l // 2):
        if s[i] != s[_l-1-i]:
            if if_palindrome(s[i+1:_l-i]):
                return i
            elif if_palindrome(s[i:_l-1-i]):
                return _l-1-i
    return -1



if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        print(str(result) + '\n')
