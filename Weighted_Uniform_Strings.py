#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the weightedUniformStrings function below.
def weightedUniformStrings(s, queries):
    _weights = {'a':1,
                'b':2,
                'c':3,
                'd':4,
                'e':5,
                'f':6,
                'g':7,
                'h':8,
                'i':9,
                'j':10,
                'k':11,
                'l':12,
                'm':13,
                'n':14,
                'o':15,
                'p':16,
                'q':17,
                'r':18,
                's':19,
                't':20,
                'u':21,
                'v':22,
                'w':23,
                'x':24,
                'y':25,
                'z':26}

    #Create a dictionary a kind of { letter: max_substring_lenght }
    _sub = {}
    _unique_sym = set(s)
    for _s in _unique_sym:
        _sub[_s] = max(list(map(len,re.findall('['+_s+']+',s))))


    #Create a result list
    _query_res = []
    for _q in queries:
        _res = 'No'
        for _sym in _sub:
            if _q >= _weights[_sym] and _q <= (_weights[_sym] * _sub[_sym]):
                if _q % _weights[_sym] == 0:
                    _res = 'Yes'
        _query_res.append(_res)



    return _query_res

if __name__ == '__main__':

    s = input()

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)


    print('\n'.join(result))
    print('\n')
