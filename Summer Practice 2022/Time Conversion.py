#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    # Write your code here
    # if they have 12 in start and Am at end, subtract 12 from start
    out = list(s)
    if ("AM" in s and s.find('12')== 0):
        out[0]= '0'
        out[1]= '0'
    elif ("PM" in s and s.find('12')!= 0):
        if (s[1] == 8):
            out[0]='2'
            out[1]='0'
        elif (s[1] == 9):
            out[0]='2'
            out[1]='1'
        else:
            out[0]=int(out[0])+1
            out[1]=int(out[1])+2
            out[0]= str(out[0])
            out[1]= str(out[1])
    
    out.pop()
    out.pop()
    result = "".join(out)
    # print(type(result))
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
