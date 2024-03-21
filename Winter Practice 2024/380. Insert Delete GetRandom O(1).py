import random
class RandomizedSet:

    def __init__(self):
        self.hash_map = {}
        self.elements = []

    def insert(self, val: int) -> bool:
        if val in self.hash_map:
            return False
        else:
            self.elements.append(val)
            self.hash_map[val] = len(self.elements)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self.hash_map:
            return False
        else:
            index = self.hash_map[val]
            le = self.elements[-1]
            self.elements[index] = le
            self.hash_map[le] = index
            self.elements.pop()
            del self.hash_map[val]
            return True

    def getRandom(self) -> int:
        return random.choice(self.elements)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()