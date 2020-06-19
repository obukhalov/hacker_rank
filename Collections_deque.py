#!/usr/bin/env python

from collections import deque

if __name__ == '__main__':
    _d = deque()
    for _ in range(int(input())):
        _input = input().split()
        if len(_input) == 2:
            eval('_d.{}({})'.format(_input[0], _input[1]))
        else:
            eval('_d.{}()'.format(_input[0] ))

    print(*_d)
