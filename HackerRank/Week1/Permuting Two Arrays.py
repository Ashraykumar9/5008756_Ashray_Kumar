#!/bin/python3

import math
import os
import random
import re
import sys


def twoArrays(p, M, N):
    # Permuting Two Arrays logic
    # Ashray_kumar_5008756
    
    aa = sorted(M)
    bb = sorted(N, reverse = True)
    for x in range(len(aa)):
        if aa[x] + bb[x] < p:
            return "NO"
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        p = int(first_multiple_input[1])

        M = list(map(int, input().rstrip().split()))

        N = list(map(int, input().rstrip().split()))

        result = twoArrays(p, M, N)

        fptr.write(result + '\n')

    fptr.close()
