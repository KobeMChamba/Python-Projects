#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    n = len(arr)
    lrd = 0
    rld = 0
    for i in range(n):
        lrd = lrd + arr[i][i]
        rld = rld + arr[i][n-1-i]
    result = lrd - rld
    if result < 0:
        return result * -1
    else:
        return result


if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonalDifference(arr))
