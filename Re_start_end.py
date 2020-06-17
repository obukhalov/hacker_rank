#!/usr/bin/env python

import re

if __name__ == '__main__':
    _S = input()
    _k = input()

#    regex = re.compile(_k)
#    if regex.search(_S):
#        _pos = 0
#        while True:
#            try:
#                match = regex.search(_S, pos = _pos)
#                _start = match.start()
#                _end = match.end() - 1
#                print((_start, _end))
#                if _start == _end:
#                    _pos = _end + 1
#                else:
#                    _pos = _end
#            except AttributeError:
#                break
#        
#    else:
#        print((-1, -1))
    if list(re.finditer('(?=({}))'.format(_k), _S)):
        for match in re.finditer('(?=({}))'.format(_k), _S):
            print((match.start(1), match.end(1) - 1))
    else:
        print((-1, -1))
