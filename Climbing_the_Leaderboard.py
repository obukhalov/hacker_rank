#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked, player):
    # Write your code here
    result = []
    scores = sorted(set(ranked), reverse=True)
    for score in player:
        while len(scores) != 0 and score >= scores[-1]:
            scores.pop()
        scores.append(score)
        result.append(len(scores))
    return result


if __name__ == "__main__":

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    print("\n".join(map(str, result)))
    print("\n")
