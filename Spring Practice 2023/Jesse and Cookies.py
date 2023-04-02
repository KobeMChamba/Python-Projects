#!/bin/python3

import math
import os
import random
import re
import sys

import bisect

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    #first solution, just brute force it
    A.sort()
    while(A[0] < k):
        if (len(A) == 1):
            break
        else:
            new_cookie = (A[0]+(A[1]*2))
            index_to_insert = bisect.bisect_left(A, new_cookie)
            A.insert(index_to_insert, new_cookie)
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
