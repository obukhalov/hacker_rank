#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the jimOrders function below.
def jimOrders(orders):
    print(orders)
    _serv = [[i+1,orders[i][0]+orders[i][1]] for i in range(len(orders))]
    _serv.sort(key=lambda x:x[1])
    _serv_time = {i[1] for i in _serv}
    _serv_time = list(_serv_time)
    _serv_time.sort()
    _serv_order = []
    for _time in _serv_time:
        _t_lst = list(filter(lambda x:x[1]==_time, _serv))
        _t_lst.sort(key=lambda x:x[0])
        for _c in _t_lst:
            _serv_order.append(_c[0])

    return _serv_order 

if __name__ == '__main__':

    n = int(input())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    print(' '.join(map(str, result)))
    print('\n')
