#!/usr/bin/env python

if __name__ == '__main__':
    _sets_collection = []
    _setA = set(input().split())
    _N = int(input())
    for i in range(_N):
        _sets_collection.append(set(input().split()))

    _strict_superset = True
    for _set in _sets_collection:
        if not _set.issubset(_setA) or len(_setA) <= len(_set):
            _strict_superset = False

    print(_strict_superset)
