#!/bin/python3

import math
import os
import random
import re
import sys


def minimumBribes(b):
    
    # New year chaos logic
    # Ashray_kumar_5008756
    
    itr = 0
    
    for x,y in enumerate(b):
        if y - 1 - x > 2:
            print("Too chaotic")
            
            return
        
        for m in range(max(y - 2, 0),x):
            if y < b[m]:
                itr = itr + 1
                temp = itr
    print(temp)
        

if __name__ == '__main__':
    p = int(input().strip())

    for p_itr in range(p):
        y = int(input().strip())

        b = list(map(int, input().rstrip().split()))
        temp1= b

        minimumBribes(temp1)
