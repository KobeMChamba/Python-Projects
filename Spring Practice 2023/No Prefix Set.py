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
        for j in range(0, i):
            #print("I: ", words[i])
            #print("J: ", words[j])
            
            prefix = False
            
            if (len(words[i]) <= len(words[j])):
                for letter_index in range(len(words[i])):
                    #print("words[i][letter_index]:", words[i][letter_index])
                    #print("words[j]:", words[j])
                    #print("letter index:", letter_index)
                    #print("words[j][letter_index]: ", end ='')
                    #print(words[j][letter_index])
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
                    print(words[i])
                    return
            else:
                for letter_index in range(len(words[j])):
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
                    print(words[i])
                    return
    print("GOOD SET")
                    
                    
                        
                        
                        
        

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
