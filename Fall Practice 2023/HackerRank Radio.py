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
    h_index = 0
    start = x[h_index]
    end = start + 1 + 2*k
    ant_count = 1
    ant_arr = [0]
    # we are at h_index = 0
    # set end = h_index + 2k
    # put down antenna
    while h_index+1 < len(x):
        print("h_index: ", h_index)
        if x[h_index+1] > end:
            print("True")
            print("end: ", end)
            ant_arr.append(h_index+1)
            ant_count +=1
            h_index +=1
            start = x[h_index]
            end = start + 1 + 2*k
        else:
            #print("Else")
            h_index +=1
    if x[-1] > end:
        ant_count +=1
        ant_arr.append(len(x)+1)
    print(ant_arr)
    return ant_count
    


# Set the array x and k here
x = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14, 18]
k = 2

# Call the function with the provided values
result = hackerlandRadioTransmitters(x, k)

# Print the result
print("result: ", result)
