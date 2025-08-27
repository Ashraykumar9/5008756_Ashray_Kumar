#!/bin/python3

import math
import os
import random
import re
import sys


def gridChallenge(table):
    
    # Grid challenge logic
    # Ashray_Kumar_5008756
    
    d = {}
    for k in range(len(table)):
        x = sorted(table[k])
        temp = x
        for l in range (len(temp)):
            value = temp[l]
            if l not in d:
                d[l] = value
            else:
                if d[l] > value:
                    return "NO"
                else:
                    value = d[l]
            
    return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input().strip())

    for s_itr in range(s):
        x = int(input().strip())

        table = []

        for _ in range(x):
            table_item = input()
            table.append(table_item)

        result = gridChallenge(table)

        fptr.write(result + '\n')

    fptr.close()
