#!/usr/bin/env python

if __name__ == '__main__':
    input()
    _eng = set(input().split())
    input()
    _fr = set(input().split())

    _all = _eng.intersection(_fr)

    print(len(_all))
