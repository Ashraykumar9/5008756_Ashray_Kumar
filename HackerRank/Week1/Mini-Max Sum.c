#!/bin/python3

import math

def miniMaxSum(arr):
    # sort the array
    arr.sort()
    # finding mini_sum 
    mininumSum = sum(arr) - arr[-1]
    # finding maxi_sum
    maximunSum = sum(arr) - arr[0]
    # show results
    print(mininumSum,maximunSum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
