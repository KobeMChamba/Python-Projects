#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    i = 0
    j = 0
    maxsum = float('-inf')
    
    while (i < 4):
        while (j < 4):
            #print("i: ", i)
            #print("j: ", j)
            top_row = 0
            bottom_row = 0
            for k in range(3):
                top_row += arr[i][j+k]
                bottom_row += arr[i+2][j+k]
            sum = top_row + bottom_row + arr[i+1][j+1]
            if sum > maxsum:
                maxsum = sum
            j += 1
        j = 0
        i += 1
    print(maxsum)
