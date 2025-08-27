#!/bin/python3

import math
import os
import random
import re
import sys


def maxMin(k, data):
    
    # Max min logic
    # Ashray_kumar_5008756
    
    value = sorted(data)
    temp = value
    
    least = temp[k - 1] - temp[0]
    temp1 = least
    
    for j in range(1, len(temp) + 1 - k):
        
        temp1 = min(temp1, temp[k - 1 + j] - temp[j])
        temp2 = temp1
    
    return temp2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    data = []

    for _ in range(n):
        data_item = int(input().strip())
        data.append(data_item)

    result = maxMin(k, data)

    fptr.write(str(result) + '\n')

    fptr.close()
