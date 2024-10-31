class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # Dummy nodes to simplify 
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: Node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def _add(self, node: Node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move the node to the front
            self._add(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # If the key is already in the cache, remove it and update its value
            self._remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            # Remove the least recently used node
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.cache[lru_node.key]

        # Add the new node (or updated node) to the front
        new_node = Node(key, value)
        self._add(new_node)
        self.cache[key] = new_node        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)