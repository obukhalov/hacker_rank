#!/usr/bin/env python

import re
import email.utils

n = int(input())
for _ in range(n):
    _name, _email = input().split()
    print('\n')
    if re.search('^[a-zA-Z][a-zA-Z0-9_\-\.]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', email.utils.parseaddr(_email)[1]):
        print('{} {}'.format(_name, _email))
