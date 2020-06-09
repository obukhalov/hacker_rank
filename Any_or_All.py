#!/usr/bin/env python

if __name__ == '__main__':
    _N = int(input())
    _line = [ i for i in input().split() ]

    print(all(map(lambda x: int(x) > 0, _line)) and any(map(lambda x: x == x[::-1], _line)))

