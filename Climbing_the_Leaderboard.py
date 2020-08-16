#!/usr/bin/env python

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(scores, alice):
    _scores = sorted(set(scores))
    _scores_len = len(_scores)
    _leaderboard = []
    _idx = 0
    for _s in alice:
        for _i in range(_idx, _scores_len):
            if _s < _scores[_i]:
                _leaderboard.append(_scores_len - _i + 1)
                _idx = _i
                break
            elif _s == _scores[_i]:
                _leaderboard.append(_scores_len - _i)
                _idx = _i
                break
            elif _s > _scores[_i]:
                if _i == _scores_len - 1:
                    _leaderboard.append(1)
                else:
                    continue
                

    return _leaderboard

if __name__ == '__main__':

    scores_count = int(input())

    scores = list(map(int, input().rstrip().split()))

    alice_count = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(scores, alice)

    print('\n'.join(map(str, result)))
    print('\n')
