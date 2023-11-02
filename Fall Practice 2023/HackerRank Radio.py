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
    ant_count = 0
    ant_arr = []
    start = 0
    passed_ant = False
    x = quicksort(x)
    print(x)
    for h_index in range(len(x)):
        print("start")
        print("h_index: ", h_index)
        if not passed_ant and x[h_index] >= (x[start] + k):
            print("adding midpoint ant")
            print("x: ", x[h_index])
            print("midpoint: ", (x[start] + k))
            ant_count += 1
            ant_arr.append(h_index)
            end = x[h_index] + k
            passed_ant = True
            print(ant_count)
        elif not passed_ant and x[h_index + 1] >= (x[start] + k):
            # next house is too far away, we need one ant for curr
            # house
            print("added ant for lonely house")
            ant_count += 1
            ant_arr.append(h_index)
            passed_ant = True
            end = x[h_index] + k
        elif passed_ant and x[h_index] > end:
            print("reached end of range")
            start = h_index
            passed_ant = False
            print(ant_count)
        if x[-1] < (x[start] + k):
            print("reached end, adding one then break")
            # if the remaining array is too small for full coverage
            ant_count += 1 
            ant_arr.append(h_index)
            print("final count: ", ant_count)
            break
    print(ant_arr)
    return ant_count

# Set the array x and k here
x = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14, 18]
k = 2

# Call the function with the provided values
result = hackerlandRadioTransmitters(x, k)

# Print the result
print("result: ", result)
