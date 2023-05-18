#!/bin/python3

import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

#
# Complete the 'reverse' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def reverse_recur(head):
    # If head is empty or has reached the list end
    if head is None or head.next is None:
        return head

    # Reverse the rest list
    rest = reverse_recur(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    # Fix the header pointer
    return rest    

def reverse(llist):
    # Iterative approach
    # Initialize pointers
    #print(llist)
    #print(llist.data)
    #print(llist.next.next.next.next.next)
    #print(llist.head)
    #print(llist.tail)

    #Iterative Solution
    '''
    my_list = SinglyLinkedList()
    my_list.head = llist
    prev = None
    current = my_list.head
    print(current)
    while (current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    my_list.head = prev
    #print("mylisthead: ", my_list.head)
    return my_list.head
    '''
    
    #Recursive Solution
    my_list = SinglyLinkedList()
    my_list.head = llist
    
    return(reverse_recur(my_list.head))
    
    
if __name__ == '__main__':