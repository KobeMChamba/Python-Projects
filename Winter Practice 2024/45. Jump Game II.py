from typing import List

class Solution:
    def next_jump(self, list, jump, jump_stack):
        # print("list: ", list)
        # print("jump: ", jump)
        # print("js: ", jump_stack)
        if list == [] or jump >= len(list):
            return jump_stack
        else:
            max_jump = 0
            max_jt = []
            for i in range(0, jump):
                if (i+list[i]) >= max_jump:
                    max_jump = (i+list[i])
                    max_jt = [i, list[i]]
            # print(max_jt)
            jump_stack.append(max_jt[1])
            return self.next_jump(list[max_jt[0]+1:], max_jt[1], jump_stack) 

    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        jump_stack = [nums[0]]
        max_dist = 0
        nums.pop(0)
        jump_stack = self.next_jump(nums, jump_stack[0], jump_stack)
        return(len(jump_stack))

# Test the code
sol = Solution()
prices = [2,0,1,1]
print("Min jumps:", sol.jump(prices))       

# Better solution (less memory usage)
# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         l = r = 0
#         res = 0
#         while r < len(nums)-1:
#             farthest = 0
#             for i in range(l, r+1):
#                 farthest = max(farthest, i+nums[i])
#             l = r + 1
#             r = farthest
#             res += 1
#         return res
#  more efficient by using 2 pointers to traverse list insted of splitting the list up