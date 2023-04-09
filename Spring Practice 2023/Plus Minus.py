#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    plus = 0
    neg = 0
    zero = 0
    
    for num in arr:
        if num > 0:
            plus = plus + 1
        elif num == 0:
            zero = zero + 1
        else:
            neg = neg + 1
    
    plus = format(plus / len(arr), ".6f")
    neg = format(neg / len(arr), ".6f")
    zero = format(zero / len(arr), ".6f")
    
    print(plus)
    print(neg)
    print(zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
