#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

    # List to store first names of people whose email address ends
    # in email_end
    matching_names = []
    for N_itr in range(N):
        first_name, email_id = input().strip().split()

        # Check if the email ID ends with the specified email_end
        if email_id.endswith("@gmail.com"):
            matching_names.append(first_name)

# Sort the list alphabetically
matching_names.sort()

# Print the sorted list of names
for name in matching_names:
    print(name)