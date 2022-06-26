#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#


def noPrefix(words):
    # Write your code here
    pref = set()
    full = set()

    for w in words:
        if w in pref:
            print("BAD SET")
            print(w)
            return
        for i in range(1, len(w) + 1):
            if w[:i] in full:
                print("BAD SET")
                print(w)
                return
            else:
                pref.add(w[:i])
        full.add(w)

    print("GOOD SET")


if __name__ == "__main__":
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
