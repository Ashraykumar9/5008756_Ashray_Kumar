#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(x):
    # set with unique char (5008756_Ashray_Kumar)
    short_term = set(x.lower()) - set(' ')
    
    # logic
    if len(short_term) == 26:
        return "pangram"
    else:
        return "not pangram" 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = input()

    result = pangrams(x)

    fptr.write(result + '\n')

    fptr.close()
