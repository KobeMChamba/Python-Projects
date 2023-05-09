#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#

def countSort(arr):
    # Write your code here
    list = [[]]
    for i, element in enumerate(arr):
        #print(element)
        #print(element[0])
        while (len(list) < int((element[0]))+1):
            list.append([])
        #print(len(list))
        if i < len(arr)/2:
            element[1] = "-"
        list[int(element[0])].append(element[1])
    #print(list)
    for arr in list:
        for element in arr:
            print(element, end=' ')
    return

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)
