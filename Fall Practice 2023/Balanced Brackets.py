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
    stack = []
    # Define a mapping of opening brackets to their corresponding closing brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in bracket_map.values():
            stack.append(char)
        elif char in bracket_map.keys():
            # If it's a closing bracket, check if the stack is empty and if the top element matches
            if not stack or stack.pop() != bracket_map[char]:
                return "NO"
        else:
            # If it's neither an opening nor closing bracket, return "NO"
            return "NO"

    # After processing the string, if the stack is empty, it's balanced
    return "YES" if not stack else "NO"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
