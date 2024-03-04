class Solution:
    def jump(self, nums: List[int]) -> int:
        jump_stack = []
        for i in range(len(nums)-2,-1,-1):
            print("i: ", nums[i])
            if nums[i] == 0:
                if jump_stack != [] and i > 0:
                    print(nums)
                    nums[i-1] -= 1
                    print(nums)
                continue
            if len(jump_stack) == 0:
                jump_stack.append(nums[i])
                print("jump_stack: ", jump_stack)
            elif nums[i] <= jump_stack[-1]:
                if i + nums[i] >= len(nums)-1:
                    jump_stack = []
                jump_stack.append(nums[i])
                print("appending: ", nums[i])
                print("jump_stack: ", jump_stack)
            else:
                print("else i: ", nums[i])
                jump_dist = 0
                counter = 0
                while jump_stack != []:
                    jump_dist += jump_stack[-1]
                    if jump_dist < nums[i]:
                        jump_stack.pop()
                        print("AP: ", jump_stack)
                        continue
                    else:
                        break
                jump_stack.append(nums[i])
                print("jump_stack: ", jump_stack)
        return(len(jump_stack))



                    
            