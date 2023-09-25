#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    max_sum = arr[0]  # Initialize the maximum sum as the first element
    current_sum = arr[0]  # Initialize the current sum as the first element
    start_index = 0  # Initialize the starting index of the maximum subarray
    end_index = 0  # Initialize the ending index of the maximum subarray
    max_subseq = arr[0]  # Initialize the maximum non-continuous sum

    print(arr)
    for i in range(1, len(arr)):
        # Update the current sum by either extending the subarray or starting a new subarray
        if arr[i] > (current_sum + arr[i]):
            #current sum is negative so start new subarr at arr[i]
            current_sum = arr[i]
            start_index = i
        else:
            #add i to the current sum
            current_sum += arr[i]
        # Update the maximum sum and ending index if the current sum is greater
        if current_sum > max_sum:
            #we kept adding elements, now we update the ending index if it actually increases the sum 
            max_sum = current_sum
            end_index = i
        #now we will look for the maximum subseq
        if (max_subseq+arr[i] > max_subseq):
            max_subseq = max_subseq+arr[i]
        if (arr[i] > max_subseq):
            max_subseq = arr[i]
            
        

    # Return the maximum subarray and subsequence
    return max_sum, max_subseq

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
