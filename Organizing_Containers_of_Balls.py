#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    _balls_in_container = [ sum(i) for i in container ]
    _balls_in_container.sort()
    _num_of_balls_of_each_color = []
    for i in range(len(container)):
        _sum = 0
        for j in range(len(container)):
            _sum += container[j][i]
        _num_of_balls_of_each_color.append(_sum)

    _num_of_balls_of_each_color.sort()


    if _balls_in_container == _num_of_balls_of_each_color:
        return 'Possible'
    else:
        return 'Impossible'

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        print(result + '\n')
