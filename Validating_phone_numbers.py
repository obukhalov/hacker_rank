#!/usr/bin/env python

import re

n = int(input())
for _ in range(n):
    if re.search('^[789][0-9]{9}$', input()):
        print('YES')
    else:
        print('NO')
    
