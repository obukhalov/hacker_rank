#!/usr/bin/env python

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    #
    # Write your code here.
    #
    if n % 2 == 0:
        _book = [ [i, i+1] for i in range(0, n + 2, 2)]
    else:
        _book = [ [i, i+1] for i in range(0, n + 1, 2)]

    _pn = 0
    if n //2 >= p:
        for i in _book:
            _pn += 1
            if p in i:
               break
    else:
        _book.reverse()
        for i in _book:
            _pn += 1
            if p in i:
                break

    return _pn - 1



if __name__ == '__main__':

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    print(str(result) + '\n')
