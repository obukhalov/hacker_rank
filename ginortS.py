#!/usr/bin/env python

if __name__ == '__main__':
    _S = input()
#    _sorted_lower = ''.join(sorted(list(filter(lambda x: x.islower(), _S))))
#    _sorted_upper = ''.join(sorted(list(filter(lambda x: x.isupper(), _S))))
#    _sorted_odd_num = ''.join(sorted(list(filter(lambda x: (int(x) % 2 == 1),list(filter(lambda x: x.isnumeric() % 2 == 1, _S))))))
#    _sorted_even_num = ''.join(sorted(list(filter(lambda x: (int(x) % 2 == 0),list(filter(lambda x: x.isnumeric() % 2 == 1, _S))))))
#    print(_sorted_lower + _sorted_upper + _sorted_odd_num + _sorted_even_num)

    print(*sorted(_S, key=lambda x: (x in '02468', x in '13579',x.isupper(),x.islower(),x)), sep='')
