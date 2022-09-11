#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# Challenge
# Given a list of integers, count and return the number of times each value appears as an array of integers.

def countingSort(arr):
    # Write your code here
    freq = [0] * 100
    for i in range(len(arr)):
        freq[arr[i]] += 1
    return freq

if __name__ == '__main__':
    sample = [0, 1, 2, 2, 3, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 7, 8, 9]
    print(countingSort(sample))