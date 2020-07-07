#!/usr/bin/env python

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        try:
            _regex = re.compile(input())
            print('True')
        except:
            print('False')

