#!/usr/bin/env python

import re
from itertools import groupby

if __name__ == '__main__':
    _cards = []
    for _ in range(int(input())):
        _cards.append(input())

    for _card in _cards:
        if re.search('(?:^[456][0-9]{15}$)|(?:^[456][0-9]{3}-[0-9]{4}-[0-9]{4}-[0-9]{4}$)', _card):
            _valid_sign = 'Valid'
            for _, _g in groupby(_card.replace('-', '')):
                if len(list(_g)) >= 4:
                    _valid_sign = 'Invalid'

        else:
            _valid_sign = 'Invalid'

        print(_valid_sign)
