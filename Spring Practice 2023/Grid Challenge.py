#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#

def gridChallenge(grid):
    # Write your code here
    grid.sort()
    #print(grid)
    for i in range(len(grid)):
        grid[i] = ''.join(sorted(grid[i]))
    #print(grid)
    for i, c in enumerate(grid[0]):
        #print(i, c)
        for string in grid[1:]:
            print("c: ", c)
            print("next: ", string[i])
            if c > string[i]:
                print(">")
                return("NO")
            c = string[i]    
    return("YES")

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()