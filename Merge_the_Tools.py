#!/usr/bin/env python

def merge_the_tools(string, k):
    # your code goes here
    for _sub_s in [ string[i: i+k] for i in range(0,len(string),k) ]:
        _new_s = ''
        while len(_sub_s) > 0:
            _new_s += _sub_s[0]
            _sub_s = _sub_s[1:].replace(_sub_s[0], '')
        print(_new_s)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
