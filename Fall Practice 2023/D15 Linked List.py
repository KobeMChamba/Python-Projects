class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self, head, data):
        if head is not None:
            new_node = Node(data)
            next = head.next
            if next is not None:
                while next.next is not None:
                    next = next.next
                next.next = new_node
            else:
                head.next = new_node
        else:
            head = Node(data)
        return head


mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
mylist.display(head); 	  