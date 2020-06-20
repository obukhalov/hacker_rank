#!/usr/bin/env python

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    s = input()
    s_dict = { i : 0 for i in set(s) }
    for _sym in s:
        s_dict[_sym] += 1

    _common_letters = [ i  for i in sorted(s_dict, key=s_dict.get, reverse=True) ]

    _result = []
    while len(_common_letters) >= 1:
        _tmp = []
        _letter = _common_letters[0]
        _letters = _common_letters.copy()
        for i in _letters:
            if s_dict[i] == s_dict[_letter]:
                _tmp.append(i)
                _common_letters.remove(i)
        for i in sorted(_tmp):
            _result.append(i)

    for i in range(3):
        print('{} {}'.format(_result[i], s_dict[_result[i]]))
