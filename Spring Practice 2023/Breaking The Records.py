#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    #print(scores)
    min = scores[0]
    max = scores[0]
    min_count = 0
    max_count = 0
    
    for num in scores[1:]:
        #print("loop")
        if num > max:
            max = num
            max_count = max_count + 1
        elif num < min:
            min = num
            min_count = min_count + 1
            
    return [max_count, min_count]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
