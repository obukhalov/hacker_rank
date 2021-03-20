#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the stringConstruction function below.
def stringConstruction(s):

    return len(set(s))



if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = stringConstruction(s)

        print(str(result) + '\n')
