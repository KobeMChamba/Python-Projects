#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    errors = 0
    i = 0
    while i < len(s):
        j = 0
        while j < 3:
            if j == 0 or j == 2:
                if s[i+j] != "S":
                    errors = errors + 1
            else:
                if s[i+j] != "O":
                    errors = errors + 1   
            j = j + 1  
        i = i + 3
    return (errors)
                                  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
