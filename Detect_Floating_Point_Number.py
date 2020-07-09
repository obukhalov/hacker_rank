#!/usr/bin/env python

import re

if __name__ == '__main__':
    for _ in range(int(input())):
        _num = input()
        #_match = re.search(r'(^[+-]{0,1}\d+\.\d+$)|(^[+-]{0,1}.\d+$)', _num)
        _match = re.search(r'(^[+-]?\d*\.\d+$)', _num)
        if _match:
            try:
                float(_num)
                print('True')
            except ValueError:
                print('False')
        else:
            print('False')

