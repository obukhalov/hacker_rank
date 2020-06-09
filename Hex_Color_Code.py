#!/usr/bin/env python

import re

if __name__ == '__main__':
    _n = int(input())
    _text = []
    _result = []
    for _ in range(_n):
        _text.append(input())

    for _str in _text:
        match = re.findall('[^\^](#[0-9a-fA-F]{3,6})', _str)
        if match:
            _result += [_color for _color in match]

    print(*_result, sep='\n')
