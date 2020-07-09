#!/usr/bin/env python

import re

if __name__ == '__main__':
    _regex = re.compile(r'(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]([AEIOUaeiou]{2,})+[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])')
    _lst = _regex.findall(input())
    if len(_lst) == 0:
        print('-1')
    else:
        print('\n'.join(_lst))
