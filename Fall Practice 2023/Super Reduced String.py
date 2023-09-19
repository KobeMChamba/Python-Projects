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
    stack = []  # Initialize an empty stack

    # Iterate through the string
    for char in s:
        # Check if the stack is not empty and the current character matches the top of the stack
        if stack and stack[-1] == char:
            stack.pop()  # Pop the character from the stack to "delete" the pair
        else:
            stack.append(char)  # Push the current character onto the stack

    # Check if the stack is empty
    if not stack:
        return "Empty String"
    else:
        return ''.join(stack)  # Construct the result string from the characters in the stack

    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
