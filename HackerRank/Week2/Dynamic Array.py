#!/bin/python3

import math
import os
import random
import re
import sys


def dynamicArray(z, searches):
    
    # Dynamic array logic
    # Ashray_kumar_5008756
    
    data = [[] for k in range(z)]
    endans = 0
    result = []
    for search in searches:
        pos = (search[1] ^ endans) % z
        if search[0] == 1:
            data[pos].append(search[2])
        elif search[0] == 2:
            endans = data[pos] [int(search[2]) % len(data[pos])]
            result.append(endans)
            temp = result
    
    return temp

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    z = int(first_multiple_input[0])

    s = int(first_multiple_input[1])

    queries = []

    for _ in range(s):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(z, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
