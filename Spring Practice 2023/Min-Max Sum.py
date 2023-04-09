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
    sum = 0
    min = arr[0]
    max = 0
    for num in arr:
        sum = sum + num
        if min > num:
            min = num
        if max < num:
            max = num
    print(sum-max, sum-min)
    #print(sum-min)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
