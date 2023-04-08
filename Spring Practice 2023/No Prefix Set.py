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

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        current.is_end_of_word = True
        
    def search(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                return False
            current = current.children[char]
            if current.is_end_of_word:
                return True
        return False

def noPrefix(words):
    trie = Trie()
    for word in words:
        if trie.search(word):
            print("BAD SET")
            print(word)
            return
        trie.insert(word)
    print("GOOD SET")

if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
