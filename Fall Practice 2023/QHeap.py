# Enter your code here. Read input from STDIN. Print output to STDOUT
Q = int(input())

# Initialize an empty heap as a list
heap = []
# Heap Functions
def heap_up(heap, i):
    while i > 0:
        parent = (i-1)//2
        if heap[i] < heap[parent]:
            #swap
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

def heap_down(heap, i, size):
    while i < size:
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i

        if left < size and heap[left] < heap[smallest]:
            smallest = left

        if right < size and heap[right] < heap[smallest]:
            smallest = right

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        else:
            break

for _ in range(Q):
    query = input().split()
    if query[0] == '1':
        # Add an element to the heap
        v = int(query[1])
        heap.append(v)
        heap_up(heap, len(heap) - 1)
    
    elif query[0] == '2':
        # Delete the element from the heap
        v = int(query[1])
        i = heap.index(v)
        heap[i] = heap[-1]
        heap.pop()
        heap_down(heap, i, len(heap))
    
    elif query[0] == '3':
        # Print the minimum of all elements in the heap
        print(heap[0])