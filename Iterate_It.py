#!/usr/bin/env python

import os
import sys
import signal

def handler(signum, frame):
    raise Exception('Timeout!')

#
# Complete the iterateIt function below.
#
def iterateIt(a):
    #
    # Write your code here.
    #
    _a = set(a)
    rep = 0
    while len(_a) > 0:
        _b = set()
        for x in _a:
            for y in _a:
                if x != y:
                    _b.add(abs(x - y))
        if _a == _b:
            return rep
        else:
            _a = _b
            rep += 1
            print('\n')
            print(len(_a))
            print(_a)

    return rep

if __name__ == '__main__':

    a_count = int(input())

    a = list(map(int, input().rstrip().split()))

#    signal.signal(signal.SIGALRM, handler)
#    signal.alarm(20)
#    try:
#        result = iterateIt(a)
#        print(str(result) + '\n')
#    except Exception:
#        print('-1')
#
#    signal.alarm(0)
    result = iterateIt(a)
    print(str(result) + '\n')
