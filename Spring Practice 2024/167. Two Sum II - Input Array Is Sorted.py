class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        index_dict = {}
        for index, num in enumerate(numbers):
            if num in index_dict:
                return [index_dict[num]+1, index+1]
            index_dict[target-num] = index
        return False
    
# Better solution
# Both solutions have have a time complexity of O(n) but this solution has a space complexity of O(1).
# def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         l = 0
#         n = len(numbers)
#         r = n - 1
#         for i in range(n):
#             if numbers[l] + numbers[r] == target:
#                 return [l+1,r+1]
#             elif numbers[l] + numbers[r] < target:
#                 l += 1
#             else:
#                 r -= 1
