#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'highestValuePalindrome' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER n
#  3. INTEGER k
#

def highestValuePalindrome(s, n, k):
    req_changes = 0
    idx_to_change = []
    idx_to_optimize = []
    if n % 2 == 0:
        #print((n/2-1))
        l_range = range(int(n/2-1), -1, -1)
        r_range = range(int(n/2), n)
    elif n >= 3:
        l_range = range(int((n-1)/2), -1, -1)
        r_range = range(int((n+1)/2), n)
    
    indexed_values = []
    for lidx, ridx in zip(l_range, r_range):
        if s[lidx] != s[ridx]:
            print("s[lidx]: ", s[lidx])
            print("s[ridx]: ", s[ridx])
            req_changes += 1
            if req_changes > k:
                return("-1")
            idx_to_change.append((lidx, ridx))
        else:
            #print("matching")
            #print(lidx)
            indexed_values.append((lidx, int(s[lidx])))
    #print(indexed_values)
            #appends (value, idx)
    sorted_indices = [index for index, value in sorted(indexed_values, key=lambda x: x[0])]
    print("sorted_indices: ", sorted_indices)
    return("test")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
