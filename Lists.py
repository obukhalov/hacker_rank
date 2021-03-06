#!/usr/bin/env python

if __name__ == '__main__':
    N = int(input())
    _cmd_lst = []
    for _ in range(N):
        _cmd_lst.append(input())

    _arr = []
    for _cmd in _cmd_lst:
        if 'insert' in _cmd:
            _c, _i, _o = _cmd.split()
            _arr.insert(int(_i), int(_o))
        elif 'print' in _cmd:
            print(_arr)
        elif 'remove' in _cmd:
            _c, _o = _cmd.split()
            _arr.remove(int(_o))
        elif 'append' in _cmd:
            _c, _o = _cmd.split()
            _arr.append(int(_o))
        elif 'sort' in _cmd:
            _arr.sort()
        elif 'pop' in _cmd:
            _arr.pop()
        elif 'reverse' in _cmd:
            _arr.reverse()
            
