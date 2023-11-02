import math
import os
import random
import re
import sys

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

def hackerlandRadioTransmitters(x, k):
    x = quicksort(x)
    print("[0, 1, 2, 3, 4, 5, 6, 7, 8,  9,  10, 11]")
    print(x)
    range = 2*k
    start = 0 
    ant_arr = [0]

    for idx, h in enumerate(x):
        if h > x[start]+range:
            start = idx
            ant_arr.append(idx)
    print(ant_arr)
    return len(ant_arr)
    


# Set the array x and k here
x = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14, 18]
x = [9, 5, 4, 2, 6, 15, 12]
k = 2

# Call the function with the provided values
result = hackerlandRadioTransmitters(x, k)

# Print the result
print("result: ", result)
