class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Initialize pointers
        i = 0
        j = 1
        j_count = 1
        while j < len(nums):
            # print("i: ", i, " | j: ", j, "jc: ", j_count)
            if nums[i] == nums[j]:
                j_count += 1
                if j_count > 2:
                    nums.pop(j)
                    # print("nums: ", nums)
                    # we removed an index so we dont have to go forward as much
                    j -= 1
            else:
                j_count = 1
                i = j
            j +=1
        return