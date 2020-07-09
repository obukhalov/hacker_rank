#!/usr/bin/env python

import math
import cmath
import re

if __name__ == '__main__':
    _x, _y = list(map(int, re.findall(r'([+-]?\d+)', input())))
    print(round(math.sqrt(_x**2 + _y**2), ndigits=3))
    print(round(cmath.phase(complex(_x,_y)), ndigits=3))
