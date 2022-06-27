#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def isValid(s):
    # Write your code here
    s_dict = {symbol: 0 for symbol in s}
    for symbol in s:
        s_dict[symbol] += 1

    s_dict_values_set = set(s_dict.values())
    s_dict_values_list = list(s_dict.values())

    if len(s_dict_values_set) > 2:
        return "NO"
    elif len(s_dict_values_set) == 1:
        return "YES"
    else:
        _min = min(s_dict_values_set)
        _max = max(s_dict_values_set)
        symbols_sum = sum(s_dict_values_list)
        if _min * len(s_dict_values_list) == symbols_sum - 1:
            return "YES"
        elif _max * (len(s_dict_values_list) - 1) == symbols_sum - 1:
            return "YES"

    return "NO"


if __name__ == "__main__":

    s = input()

    result = isValid(s)

    print(result + "\n")
