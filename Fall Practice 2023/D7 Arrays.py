#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    string = ""
    for element in arr:
        string = string + str(element) + " "
    string = string[:-1]
    print(string)
        