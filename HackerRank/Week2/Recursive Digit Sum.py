#!/bin/python3

import math
import os
import random
import re
import sys


def superDigit(a, b):
    
    # Recursive digit sum logic
    # Ashray_Kumar_5008756
    
    # multipy by b
    overall = str(sum(int(value) for value in a)*b)
    
    # until a single digit
    while len(overall)>1:
        overall = str(sum(int(value) for value in overall))
        
        temp = overall
        
    return int(temp)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    a = first_multiple_input[0]

    b = int(first_multiple_input[1])

    result = superDigit(a, b)

    fptr.write(str(result) + '\n')

    fptr.close()
