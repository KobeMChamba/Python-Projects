#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            #print("I: ", words[i])
            #print("J: ", words[j])
            
            prefix = False
            
            if (len(words[i]) <= len(words[i])):
                for letter_index in range(len(words[i])):
                    if (words[i][letter_index] != words[j][letter_index]):
                        prefix = False
                        #print("They differ at letter index: ", letter_index)
                        break
                        
                    else:
                        prefix = True
                        continue
                if prefix:
                    print("BAD SET")
                    #print(words[i])
                    print(words[j])
                    return
            else:
                for letter_index in range(len(words[j])):
                    if (words[i][letter_index] != words[j][letter_index]):
                        prefix = False
                        print("They differ at letter index: ", letter_index)
                        break
                    else:
                        prefix = True
                        continue
                if prefix:
                    print("BAD SET")
                    #print(words[i])
                    print(words[j])
                    return
    print("GOOD SET")
                    
                    
                        
                        
                        
        

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
