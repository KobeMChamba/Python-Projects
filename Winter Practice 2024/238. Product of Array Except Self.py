class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod_arr = nums.copy()
        prod_arr[-2] = nums[-1]
        prod_arr[-1] = 1
        for i in range(len(prod_arr)-3, -1, -1):
            prod_arr[i] = prod_arr[i+1] * nums[i+1]
        print("pa: ", prod_arr)
        prev = nums[0]
        for i in range(1, len(prod_arr)):
            prod_arr[i] = prod_arr[i] * prev
            prev = nums[i]*prev
        return prod_arr