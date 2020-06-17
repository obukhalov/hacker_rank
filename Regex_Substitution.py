#!/usr/bin/env python

import re

if __name__ == '__main__':
    _input = ''
    for _ in range(int(input())):
        _input += input() + '\n'

    _input = re.sub(r'(?<= )&&(?= )', 'and', _input, re.DOTALL)
    _input = re.sub(r'(?<= )\|\|(?= )', 'or', _input, re.DOTALL) 

    print(_input)
