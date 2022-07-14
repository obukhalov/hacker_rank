#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#


def minimumLoss(price):
    # Write your code here

    # Remember original price indexes
    idx = {p: i for i, p in enumerate(price)}

    # Sort price list for place closest numbers next to each other
    price.sort()

    min_loss = 10 ** 16
    for i in range(len(price) - 1):
        p1 = price[i]
        i1 = idx[p1]
        p2 = price[i + 1]
        i2 = idx[p2]

        if i2 < i1:
            loss = p2 - p1

            if loss < min_loss:
                min_loss = loss

    return min_loss


if __name__ == "__main__":

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    print(str(result) + "\n")
