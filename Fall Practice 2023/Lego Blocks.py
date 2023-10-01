#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    f = [1]
    g = [1]
    h = [1]
    for i in range(1, m + 1):
        sumhg = 0
        for j in range(1, i):
            sumhg += h[j] * g[i-j] % (10**9+7)
        f.append(sum(f[-4:]) % (10**9+7))    
        g.append(f[i] ** n % (10**9+7))
        h.append((g[i] - sumhg) % (10**9+7))
    return h[-1] % (10**9+7)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
