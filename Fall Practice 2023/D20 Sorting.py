#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    numSwaps = 0
    numOfSwaps = 0
    for i in range(n):
        numSwaps += numOfSwaps
        numOfSwaps = 0
        for j in range(n-1):
            #swap adjacent elements if they are in decreasing order
            if (a[j] > a[j+1]):
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                numOfSwaps += 1
        if numOfSwaps == 0:
            break
    ## end of bubble sort
    firstel = a[0]
    lastel = a[-1]
    
    print("Array is sorted in", numSwaps, "swaps.")
    print("First Element:", firstel)
    print("Last Element:", lastel)
    