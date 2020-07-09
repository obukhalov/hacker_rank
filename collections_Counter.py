#!/usr/bin/env python

from collections import Counter

if __name__ == '__main__':
    _ = input()
    _shoes_dict = Counter(input().split())
    _money = 0
    for _ in range(int(input())):
        _size, _price = input().split()
        if _shoes_dict[_size] != 0:
            _money += int(_price)
            _shoes_dict[_size] -= 1

    print(_money)
