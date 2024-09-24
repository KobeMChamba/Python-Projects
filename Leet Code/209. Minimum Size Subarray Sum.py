class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        total = 0
        min_length = float('inf')
            
        for j in range(len(nums)):
            total += nums[j]
                
            while total >= target:
                min_length = min(min_length, j - i + 1)
                total -= nums[i]
                i += 1
            
        return min_length if min_length != float('inf') else 0