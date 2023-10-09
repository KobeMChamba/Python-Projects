#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    answers = []
    prev_letter = None
    counter = 1
    letter_dict = {}
    letter_to_value = {
    'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
    'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
    'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
    'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
    'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

    #print("len(s): ", len(s))
    for i in range(0, len(s)):
        #print(i)
        #print("scanned letter: ", s[i])
        if s[i] == prev_letter:
            counter = counter + 1
        elif prev_letter is not None:
            #print("cl: ", s[i])
            if prev_letter not in letter_dict:
                letter_dict[prev_letter] = counter
            elif counter > letter_dict[prev_letter]:
                letter_dict[prev_letter] = counter
            prev_letter = s[i]
            counter = 1
        else:
            #prev_letter is None
            prev_letter = s[i]
            counter = 1
            
        if i == (len(s)-1):
            #print("i==len(s")
            if s[i] not in letter_dict:
                letter_dict[s[i]] = counter
            elif counter > letter_dict[s[i]]:
                letter_dict[s[i]] = counter
    
    
    # print("Letter_dict")
    # for key in letter_dict.keys():
    #     print(key, ": ", letter_dict[key])
    # print("done")
    
    for q in queries:
        #print("q: ", q)
        q_ans = "No"
        for key in letter_dict.keys():
            #print("key: ", key)
            if divisible(q, letter_to_value[key]):
               #print("divisible")
                if (q/letter_to_value[key]) <= letter_dict[key]:
                    #print("YES\n")
                    q_ans = "Yes"
                    break
                    
        answers.append(q_ans)
    #print("answers: ", answers)
    return answers

def divisible(a, b):
    if a % b == 0:
        return True
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
