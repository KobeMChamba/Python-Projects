#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    # Write your code here
    string = ""
    mod_k = k % 26
    for char in s:
        print("For loop for: " + char)
        asc = ord(char)
        if asc >= 65 and asc <=90:
            print("First")
            print(asc)
            enc = (ord(char)+mod_k)
            if (enc > 90):
                enc = enc - 26
            enc = chr(enc)
        elif (asc >= 97 and asc <=122):
            print("Second")
            enc = (ord(char)+mod_k)
            if (enc > 122):
                enc = enc - 26
            enc = chr(enc)
        else:
            print("else")
            enc=char
        string=string+enc
    print(string)
    return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
