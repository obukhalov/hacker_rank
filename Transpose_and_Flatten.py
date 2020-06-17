#!/usr/bin/env python

import numpy

if __name__ == '__main__':
    _N, _M = list(map(int, input().split()))
    _input = []
    for _ in range(_N):
        _input.append(list(map(int, input().split())))

    print(numpy.transpose(numpy.array(_input)))
    print(numpy.array(_input).flatten())
