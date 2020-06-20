#!/usr/bin/env python

if __name__ == '__main__':
    _result = []
    for _ in range(int(input())):
        _n = int(input())
        _cubes = list(map(int, input().split()))
        _stack = []

        while len(_cubes) >= 1:
            if len(_stack) == 0:
                if _cubes[0] >= _cubes[-1]:
                    _stack.append(_cubes[0])
                    _cubes.pop(0)
                else:
                    _stack.append(_cubes[-1])
                    _cubes.pop(-1)
            else:
                if _cubes[0] >= _cubes[-1] and _cubes[0] <= _stack[-1]:
                    _stack.append(_cubes[0])
                    _cubes.pop(0)
                elif _cubes[-1] <= _stack[-1]:
                    _stack.append(_cubes[-1])
                    _cubes.pop(-1)
                else:
                    break

        if len(_stack) == _n:
            _result.append('Yes')
        else:
            _result.append('No')

    print(*_result, sep='\n')


