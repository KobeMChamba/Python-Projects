class Solution:
    def swap(self, left, right, arr):
        while left < right:
            # Swap elements at positions left and right
            arr[left], arr[right] = arr[right], arr[left]
            # Move left pointer to the right
            left += 1
            # Move right pointer to the left
            right -= 1
        return
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.swap(0, len(nums) - 1, nums)
        # invert halves
        self.swap(0, k-1, nums)        
        self.swap(k, len(nums) - 1, nums)
        return nums

