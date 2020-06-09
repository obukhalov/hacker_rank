#!/usr/bin/env python

import re

if __name__ == '__main__':
    _UID_list = []
    for i in range(int(input())):
        _UID_list.append(input())

    for _UID in _UID_list:
        _valid_sign = 'Invalid'
        match = re.search('[a-zA-Z0-9]{10}', _UID)
        if match and len(_UID) == len(set(_UID)) and len(re.findall('[0-9]', _UID)) >= 3 and len(re.findall('[A-Z]', _UID)):
            _valid_sign = 'Valid'
        print(_valid_sign)
                



