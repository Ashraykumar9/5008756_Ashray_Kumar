#!/bin/python3

import math
import os
import random
import re
import sys



def isBalanced(b):
    
    # Balanced brackets logic
    # Ashray_kumar_5008756
    
    for k in range(len(b)):
        
        a = b.replace('()','')
        temp = a
        
        t = temp.replace('[]','')
        temp1 = t
        
        b = temp1.replace('{}','')
    
    return "YES" if len(b) == 0 else "NO"
    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    r = int(input().strip())

    for r_itr in range(r):
        b = input()

        result = isBalanced(b)

        fptr.write(result + '\n')

    fptr.close()
