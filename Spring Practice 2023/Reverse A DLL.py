#!/bin/python3

import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_DOUBLY_LINKED_LIST.
# The function accepts INTEGER_DOUBLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#

def reverse(llist):
    # Write your code here
    # Iterative solution
    # Traverse the linked list using a pointer
    # Swap the prev and next pointers for all nodes
    # At last, change the head pointer of the doubly linked list
    print(llist)
    print(llist.data)
    print(llist.next)
    print(llist.prev)
    
    #Create list, this is not needed but makes it easier for me to understand the structure
    reversed_dll = DoublyLinkedList()
    
    temp = None
    # Create traversal pointer
    current = llist
    # Traverse and swap prev and next pointers for all nodes
    while current != None:
        temp = current.prev
        current.prev = current.next
        current.next = temp
        # Go on to "next" node
        current = current.prev
        
    # Before changing head, check for the cases like
    # empty list and list with only one node
    # empty list will mean temp is none and we do not need to change head
    # one node means temp will point to prev which will be none, no need to change head
    if temp is not None:
        reversed_dll.head = temp.prev
        return reversed_dll.head
    else:
        return llist    

if __name__ == '__main__':