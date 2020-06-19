#!/usr/bin/env python

from collections import OrderedDict
import re

if __name__ == '__main__':
    _items = OrderedDict()
    for _ in range(int(input())):
        match = re.search(r'(.*)\s(\d+)', input())
        if match:
            if _items.get(match.group(1)):
                _items[match.group(1)] += int(match.group(2))
            else:
                _items[match.group(1)] = int(match.group(2))


    print('\n\n\n', *[ '{} {}'.format(_key, _items[_key]) for _key in _items ], sep='\n' )



