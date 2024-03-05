from typing import List

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        # print(citations)
        for i in range(len(citations), 0, -1):
            if citations[i-1] >= i:
                print(citations[i-1])
                print(i)
                return i
        return 0

# Test the code
sol = Solution()
tl = [1,3,1]
print("H Index:", sol.hIndex(tl))     

# Better solution
# Very similar but just uses simpler logic 
# class Solution:
#     def hIndex(self, citations: List[int]) -> int:
        
#         citations.sort(reverse=True)
#         i = 0
        
#         while i < len(citations) and i < citations[i]:
#             i += 1
            
#         return i
    
