#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    stack = [0]  # Initialize a stack with the first bar's index
    S = 0       # Initialize a variable to store the maximum area
    maxS = 0    # Initialize the maximum area as 0
    h.append(0)  # Append a zero to the end of the histogram (used to process the remaining bars)

    for i in range(1, len(h)):
        if h[i] >= h[stack[-1]]:
            # If the current bar's height is greater or equal to the height of the bar at the top of the stack,
            # push the current bar's index onto the stack.
            stack.append(i)
        else:
            # If the current bar's height is smaller than the height of the bar at the top of the stack,
            # it means we can no longer extend the rectangle to the right with bars in the stack.

            while stack and h[i] < h[stack[-1]]:
                # While the stack is not empty and the current bar's height is smaller than the height of the bar at the top of the stack:

                last = stack.pop()  # Pop the index of the bar at the top of the stack (the shortest bar)
                if stack:
                    # If there are still bars in the stack, calculate the area of the rectangle using
                    # the current index `i` and the previous index in the stack.
                    S = (i - stack[-1] - 1) * h[last]
                else:
                    # If the stack is empty, it means we calculate the area using all bars from index 0 to `i`.
                    S = i * h[last]

                if S > maxS:
                    maxS = S  # Update the maximum area if the newly calculated area is larger.

            stack.append(i)  # Push the current index onto the stack to continue the process.

    return maxS  # Return the maximum area found in the histogram.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
