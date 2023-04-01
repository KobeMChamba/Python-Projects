# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

class QueueWithTwoStacks:
    def __init__(self):
        self.stack_enqueue = []
        self.stack_dequeue = []

    def enqueue(self, item):
        self.stack_enqueue.append(item)

    def dequeue(self):
        if not self.stack_dequeue:
            while self.stack_enqueue:
                self.stack_dequeue.append(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

    def is_empty(self):
        return len(self.stack_enqueue) == 0 and len (self.stack_dequeue) == 0

    def size(self):
        return len(self.stack_enqueue) + len(self.stack_dequeue)

queue = QueueWithTwoStacks()
        
for _ in range(int(input())):
    val = list(map(int,input().split()))
    #print("enq:", queue.stack_enqueue)
    #print("deq:", queue.stack_dequeue)
    if val[0] == 1:
        #print("1", val[1])
        queue.enqueue(val[1])
    elif val[0] == 2:
        #print("2")
        queue.dequeue()
    else:
        #print(3)
        if queue.stack_dequeue:
            print(queue.stack_dequeue[-1])
        else:
            print(queue.stack_enqueue[0])
    
    
