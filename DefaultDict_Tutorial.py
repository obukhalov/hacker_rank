#!/usr/bin/env python

from collections import defaultdict

if __name__ == '__main__':
    _n, _m = list(map(int, input().split()))

    _n_dict = defaultdict(list)

    for i in range(_n):
        _n_dict[input()].append(i + 1)

    for i in range(_m):
        _el = input()
        if _n_dict[_el]:
            print(*_n_dict[_el], sep=' ')
        else:
            print(-1)
