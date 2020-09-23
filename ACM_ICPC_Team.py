#!/usr/bin/env python

import math
import os
import random
import re
import sys
from itertools import combinations

# Complete the acmTeam function below.
def acmTeam(topic):
    _res_dict = {}
    for _comb in combinations(range(len(topic)), 2):
        _num = bin(int(topic[_comb[0]], base=2) | int(topic[_comb[1]], base=2)).count('1')
        if not _res_dict.get(_num):
            _res_dict[_num] = [_comb]
        else:
            _res_dict[_num].append(_comb)

    return [ max(_res_dict), len(_res_dict[max(_res_dict)]) ]

if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)

    result = acmTeam(topic)

    print('\n'.join(map(str, result)))
    print('\n')
