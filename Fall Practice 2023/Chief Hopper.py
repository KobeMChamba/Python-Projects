#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chiefHopper' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def chiefHopper(arr):
    #initialize energy
    needed_energy=0
    #reverse list
    arr.reverse()
    for i in arr:
        #go through each height
        #calculate needed energy for this height, set previous NE as goal
        needed_energy=math.ceil((needed_energy+i)/2)
    return needed_energy
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = chiefHopper(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
