#!/usr/bin/env python

from collections import OrderedDict

if __name__ == '__main__':
    _words = OrderedDict()
    for _ in range(int(input())):
        _word = input()
        if _words.get(_word):
            _words[_word] += 1
        else:
            _words[_word] = 1

    print(len(_words)) 
    print(*_words.values())

