class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left = 0
        right = N-1
        left_max = 0
        right_max = 0
        waters = 0
        while left < right:
            # print("Loop")
            # print("L: ", left)
            # print("R: ", right)
            if height[left] < height[right]:
                # print("L<R")
                if height[left] <= left_max:
                    # print("Add water")
                    waters += left_max - height[left]
                    # print("W: ", waters)
                else:
                    # print("Update max")
                    left_max = height[left]
                left += 1
            else:
                # print("R>=L")
                if height[right] <= right_max:
                    # print("Add water")
                    waters += right_max - height[right]
                    # print("W: ", waters)
                else:
                    # print("Update max")
                    right_max = height[right]
                right -= 1
        return waters
