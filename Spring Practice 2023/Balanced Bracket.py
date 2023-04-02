#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    op = []
    for i in range(len(s)):
        if s[i] in '({[':
            op.append(s[i])
        elif s[i] in ')}]':
            try:
                if op[-1]+s[i] == '()' or op[-1]+s[i] == '{}' or op[-1]+s[i] == '[]':
                    op.pop(-1)
                else:
                    return 'NO'
            except:
                return 'NO'
    if len(op) != 0:
        return 'NO'
    else:
        return 'YES'
                        
                
                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
