#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superReducedString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
    
def superReducedString(s):
    print("s: ", s)
    original_s = s
    if s == "":
        return "Empty String"
    prev = None
    ##while loop here
    for index, char in enumerate(s):
        print("index: ", index)
        print("char: ", char)
        if char == prev:
            print("IST")
            print("   s: ", s)
            s = s[:(index-1)]+s[(index+1):]
            print("   s: ", s)
        prev = char
    if original_s == s:
        print("Final")
        print("s:", s)
        #s = s.replace(" ", "")
        #print("s:", s)
        print(type(s))
        return s
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()