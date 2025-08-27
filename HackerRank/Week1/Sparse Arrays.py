#!/bin/python3

import math
import os
import random
import re
import sys


def maSt(s, q):
    
    #  Sparse arrays logic
    # Ashray_kumar_5008756
    
    out = []
    
    for x in range(len(q)):
        c = 0
        for y in range(len(s)):
            if q[x] == s[y]:
                c = c + 1
        out.append(c)
    return out 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s_c = int(input().strip())

    s = []

    for _ in range(s_c):
        s_i = input()
        s.append(s_i)

    q_c = int(input().strip())

    q = []

    for _ in range(q_c):
        q_i = input()
        q.append(q_i)

    res = maSt(s, q)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
