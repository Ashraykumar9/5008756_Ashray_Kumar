#!/bin/python3

import math
import os
import random
import re
import sys


def climbingLeaderboard(level, gamer):
    
    # Climbing the leaderboard logic
    # Ashray_Kumar_5008756
    
    out = []
    count = sorted(list(set(level)))
    k = 0
    distance = len(count)
    for t in gamer:
        while distance > k and t >= count[k]:
            k = k + 1
        out.append(distance - k + 1)
        temp = out
    
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    level_count = int(input().strip())

    level = list(map(int, input().rstrip().split()))

    gamer_count = int(input().strip())

    gamer = list(map(int, input().rstrip().split()))

    output = climbingLeaderboard(level, gamer)

    fptr.write('\n'.join(map(str, output)))
    fptr.write('\n')

    fptr.close()
