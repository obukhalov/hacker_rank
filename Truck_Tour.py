#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'truckTour' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY petrolpumps as parameter.
#


def truckTour(petrolpumps):
    # Write your code here

    _len = len(petrolpumps)

    for i in range(_len):
        petrol = 0
        distance = 0
        stop = False

        for j in range(i, _len):
            petrol += petrolpumps[j][0]
            distance += petrolpumps[j][1]
            if distance > petrol:
                stop = True
                break

        if stop == False:

            for j in range(i):
                petrol += petrolpumps[j][0]
                distance += petrolpumps[j][1]
                if distance > petrol:
                    stop = True
                    break

        if stop == False:
            return i


if __name__ == "__main__":

    n = int(input().strip())

    petrolpumps = []

    for _ in range(n):
        petrolpumps.append(list(map(int, input().rstrip().split())))

    result = truckTour(petrolpumps)

    print(str(result) + "\n")
