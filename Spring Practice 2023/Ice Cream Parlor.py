#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'icecreamParlor' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER m
#  2. INTEGER_ARRAY arr
#

def icecreamParlor(m, arr):
    # Write your code here
    complement_map = {}  # dictionary to store complement of elements
    for index, num in enumerate(arr):
        complement = m - num
        #checks all keys for complement
        if complement in complement_map:
            #index represents the num
            #answer should be 1-based indexing
            return [complement_map[complement]+1, index+1]
        else:
            complement_map[num] = index

    return []  # no pair found

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        m = int(input().strip())

        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = icecreamParlor(m, arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()