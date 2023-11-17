#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    n = bin(n)
    max = 0
    count = 0
    for b in n:
        if b == "1":
            count += 1
            if count > max:
                max = count
        else:
            count = 0
    print(max)
    
    