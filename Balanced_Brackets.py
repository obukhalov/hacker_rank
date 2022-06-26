#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


class Balance:
    def __init__(self):
        self.sign = True
        self.brackets = {"{": "}", "[": "]", "(": ")"}

    def isBalanced_recursive(self, s):
        if len(s) == 0:
            pass
        else:
            if s[0] in ")]}":
                self.sign = False
            else:
                op = s[0]
                cl = self.brackets[op]
                count = 1
                for i in range(1, len(s)):
                    if s[i] == op:
                        count += 1
                    elif s[i] == cl:
                        count -= 1
                        if count == 0:
                            s1 = s[1:i]
                            s2 = s[i + 1 :]
                            self.isBalanced_recursive(s1)
                            self.isBalanced_recursive(s2)
                            break
                if count != 0:
                    self.sign = False


def isBalanced(s):
    # Write your code here
    balance = Balance()
    balance.isBalanced_recursive(s)
    if balance.sign == True:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result + "\n")
