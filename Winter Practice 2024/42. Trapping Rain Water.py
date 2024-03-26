class Solution:
    def trap(height):
    total_water = 0
    stack = []

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top_index = stack.pop()
            if not stack:
                break
            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[top_index]
            total_water += distance * bounded_height
        stack.append(i)

    return total_water

