#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'alternate' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def alternate(s):
    max_length = 0
    unique_chars = set(s)
    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                # Ensure that char1 < char2 to avoid duplicate testing
                if char1 < char2:
                    filtered_str = [c for c in s if c == char1 or c == char2]
                    if all(filtered_str[i] != filtered_str[i + 1] for i in range(len(filtered_str) - 1)):
                        max_length = max(max_length, len(filtered_str))

    return max_length

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
