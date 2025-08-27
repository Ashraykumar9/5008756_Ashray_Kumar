#!/bin/python3

import math
import os
import random
import re
import sys


def balancedSums(data):
    
    # Sherlock and array logic
    # Ashray_Kumar_5008756
    
    invalid = 0
    valid = sum(data)
    
    for digit in data:
        
        valid = valid - digit
        
        if valid == invalid:
            return "YES"
        
        invalid = invalid + digit
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        data = list(map(int, input().rstrip().split()))

        result = balancedSums(data)

        fptr.write(result + '\n')

    fptr.close()
