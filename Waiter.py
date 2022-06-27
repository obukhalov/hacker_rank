#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#


def waiter(number, q):
    # Write your code here
    # Get a list of the first q prime numbers
    primes = []
    for num in range(2 ** 32):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
        if len(primes) == q:
            break

    answers = []
    A = number.copy()
    B = []
    A_tmp = []
    B_tmp = []

    for pr in primes:
        A_tmp.clear()
        B_tmp.clear()

        for num in A[::-1]:
            if num % pr == 0:
                B_tmp.append(num)
            else:
                A_tmp.append(num)
        A = A_tmp.copy()
        B = B_tmp.copy()
        answers.extend(B[::-1])

    answers.extend(A[::-1])

    return answers


if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    print("\n".join(map(str, result)))
    print("\n")
