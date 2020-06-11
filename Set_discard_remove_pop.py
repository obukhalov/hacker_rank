#!/usr/bin/env python

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))

    for _ in range(int(input())):
        _cmd = input()
        if 'pop' in _cmd:
            try:
                s.pop()
            except KeyError:
                pass
        elif 'remove' in _cmd:
            try:
                s.remove(int(_cmd.split()[1]))
            except KeyError:
                pass
        elif 'discard' in _cmd:
            s.discard(int(_cmd.split()[1]))

    print(sum(s))
