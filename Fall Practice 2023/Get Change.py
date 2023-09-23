#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):

    # Create a table to store the number of ways to make change for each amount from 0 to n
    dp = [0] * (n + 1)

    # There's one way to make change for zero: by not using any coin
    dp[0] = 1

    # Iterate through the denominations
    for coin in c:
        # Update the table for each amount from coin to n
        for amount in range(coin, n + 1):
            dp[amount] += dp[amount - coin]

    # The last cell in dp contains the number of ways to make change for the given amount
    return dp[n]

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()
