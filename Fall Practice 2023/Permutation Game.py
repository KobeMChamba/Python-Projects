#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationGame' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def permutationGame(arr):
    #Simple lambda function that returns true if all items are in increasing order
    isIncreasing = lambda arr: all([arr[i] < arr[i + 1] for i in range(len(arr) - 1)])
    
    memo = {}
 
    def findWinner(arr):
        print("findWinner")
        print("memo: ", memo)
        key = tuple(arr)
        print("key: ", key)
        if key in memo:
            print("key in memo")
            return memo[key]
        
    # If arr is ascending, then this player wins (base case)
        if isIncreasing(arr):
            print("is increasing, adding true to memo")
            memo[key] = True
            return True
    
    # Calculate next turns: If next player has any available winning moves, this player lost
    #You check if the player can make a move that makes the other player lose
        for idx in range(len(arr)):
            print("removed idx: ", arr[idx], "arr=: ", arr[:idx] + arr[idx + 1:])
            #if findwinner, aka if next step leads to the other player winning, the previous state leads to a loss for the current player
            if findWinner(arr[:idx] + arr[idx + 1:]):
                print("findwinner was true")
                print("memo[key]: ", key)
                print("adding to memo: False")
                memo[key] = False
                return False
            
    # Otherwise, this player wins because next player has no winning moves available
        memo[key] = True
        print("memo[key]: ", key)
        print("adding to memo: True")
        return True
   
    
    ans = "Bob"
    if not findWinner(arr):
        ans = "Alice"
    print("returning: ", ans)
    return ans
    #return 'Bob' if findWinner(arr) else 'Alice'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = permutationGame(arr)

        fptr.write(result + '\n')

    fptr.close()
