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
    # Write your code here
    # N: Height
    # M: Width

#should be recursive
    #base case
    if n == 0:
        return 1
    
    #recursive case
    total_permutations = 0
    #for each block size
    for size in [1, 2, 3, 4]:
        if m >= size:
            # add brick to wall
            new_wall = [[0]*m for _ in range(n)]
            for i in range(n):
                for j in range(m-size+1):
                    if all(row[j:j+size] == [0]*size for row in new_wall[:i]):
                        # add brick to wall
                        for k in range(j, j+size):
                            new_wall[i][k] = 1
                        # count permutations with new brick added
                        total_permutations += legoBlocks(n, m-size)
    

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
