#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stockmax' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY prices as parameter.
#

def stockmax(prices):  
    profit = 0
    while len(prices) > 1:
        # Find the index of the maximum price
        max_price_index = prices.index(max(prices))
        
        # Buy one stock each day before the maximum price
        for i in range(max_price_index):
            profit -= prices[i]
        
        # Sell all stocks on the maximum day
        profit += len(prices[:max_price_index]) * prices[max_price_index]
        
        # Update prices for the remaining days
        prices = prices[max_price_index + 1:]
    
    return profit
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        prices = list(map(int, input().rstrip().split()))

        result = stockmax(prices)

        fptr.write(str(result) + '\n')

    fptr.close()
