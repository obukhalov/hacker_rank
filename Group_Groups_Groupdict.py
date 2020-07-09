#!/usr/bin/env python

import re

if __name__ == '__main__':
    _match = re.search(r'([0-9a-zA-Z])\1+', input())
    if _match:
        print(_match.group(1))
    else:
        print('-1')
