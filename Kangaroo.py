#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    x1v1 = x1 + v1
    x2v2 = x2 + v2
    if x1v1 == x2v2:
        return 'YES'
    else:
        distance = abs(x1v1 - x2v2)
        while True:
            x1v1 += v1
            x2v2 += v2
            if x1v1 == x2v2:
                return 'YES'
            elif abs(x1v1 - x2v2) >= distance:
                return 'NO'
            else:
                distance = abs(x1v1 - x2v2)

            



if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    print(result + '\n')
