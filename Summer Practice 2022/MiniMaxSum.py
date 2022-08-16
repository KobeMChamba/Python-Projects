#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    # min = arr[0]+arr[1]+arr[2]+arr[3]+arr[4]
    # max = 0
    # for num in arr:
    #     #num is ignored
    #     sum = 0
    #     for eonum in arr:
    #         if eonum != num:
    #            sum = sum + eonum
    #     # adds up every other number
    #     if sum >= max:
    #         max = sum
    #     if sum <= min :#or min == 0:
    #         min = sum
            
    min = 0
    max = 0
    
            
    print(min, max)
        
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
