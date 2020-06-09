#!/usr/bin/env python

from itertools import groupby

if __name__ == '__main__':
    _S = input()
    for _k, _g in groupby(_S):
        print('({}, {})'.format(len(list(_g)), _k), end=' ')

