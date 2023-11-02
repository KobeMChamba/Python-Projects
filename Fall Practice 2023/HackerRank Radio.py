import math
import os
import random
import re
import sys

def hackerlandRadioTransmitters(x, k):
    x.sort()
    count = 0
    while x:
        leftHouse = x[0]
        while x and leftHouse+k >= x[0]:
            transmitter=x.pop(0)
        while x and transmitter+k >= x[0]:
            x.pop(0)
        count += 1    
    return count


# Set the array x and k here
x = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 14, 18]
x = [9, 5, 4, 2, 6, 15, 12]
k = 2

# Call the function with the provided values
result = hackerlandRadioTransmitters(x, k)

# Print the result
print("result: ", result)
