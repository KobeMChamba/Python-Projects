class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = self.computeDifference()
        
    def computeDifference(self):
        if len(self.__elements) < 2:
            return None
        # Handle the case where the list has less than two elements

        min_element = self.__elements[0]
        max_element = self.__elements[0]
        
        for num in self.__elements[1:]:
            if num < min_element:
                min_element = num
            if num > max_element:
                max_element = num
        return max_element - min_element

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)