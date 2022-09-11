#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
def lonelyinteger(a):
    for i in range(len(a)):
        #print("i: "+ str(i))
        for j in range(len(a)):
            #print("j: "+ str(j))
            if (j == len(a) - 1 and i == len(a) - 1):
                #print("first")
                return a[i]
            elif (j == i and len(a) != 1):
                #print("pass, same spot")
                pass
            elif (a[i] == a[j]):
                #print("break, match found")
                break
            elif (j == len(a)-1):
                return a[i]
            #print("end of j loop \nj was: " + str(j))
        #print("end of i loop \ni was: " + str(i))

if __name__ == '__main__':
    array = [0, 0, 1, 2, 1]
    print(lonelyinteger(array))