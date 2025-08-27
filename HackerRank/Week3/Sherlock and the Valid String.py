#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


def isValid(v):
    
    # Sherlock and the valid string logic
    # Ashray_kumar_5008756
    
    a = Counter(v.lower())
    temp = a
    total = list(temp.values())
    temp1 = total
    if len(set(temp1)) == 1:
        return 'YES'
    temp1.sort()
    
    if temp1[0] == 1 and len(set(temp1[1:])) == 1:
        return 'YES'
    temp1[-1] = temp1[-1] - 1
    
    if len(set(temp1)) == 1:
        return 'YES'
    return 'NO'
     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    v = input()

    result = isValid(v)

    fptr.write(result + '\n')

    fptr.close()
