#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def anagram(s):
    # Write your code here
    if len(s) % 2 == 1:
        return -1
    else:
        half_s = len(s) // 2
        left = s[:half_s]
        right = s[half_s:]
        unique_letters_in_left = set(left)
        counter = 0
        for letter in unique_letters_in_left:
            left_letter_counter = left.count(letter)
            right_letter_counter = right.count(letter)
            if left_letter_counter > right_letter_counter:
                difference = left_letter_counter - right_letter_counter
                counter += difference
    return counter


if __name__ == "__main__":

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        print(str(result) + "\n")
