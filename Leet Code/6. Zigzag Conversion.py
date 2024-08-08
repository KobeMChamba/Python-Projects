class Solution:
    def zigzag(self, n):
        current = 0
        step = 1

        while True:
            yield current
            current += step

            if current == n - 1 or current == 0:
                step = -step

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        ans = [[] for _ in range(numRows)]
        z = self.zigzag(numRows)
        
        for char in s:
            row = next(z)
            ans[row].append(char)
        
        result = ''.join([''.join(row) for row in ans])
        return result
    
# Most efficient solution
# class Solution:
#     def convert(self, s: str, numRows: int) -> str:
#         if(numRows  < 2):
#             return s
#         arr = ['' for i in range(numRows)]
#         direction = 'down'
#         row = 0
#         for i in s:
#             arr[row] += i
#             if row == numRows-1:
#                 direction = 'up'
#             elif row == 0:
#                 direction = 'down'
#             if(direction == 'down'):
#                 row += 1
#             else:
#                 row -= 1
#         return(''.join(arr))

# While my code is more readable this code makes sure to include the case if  numRows is 1
# and is a little bit more efficient as it adds directly to each point in the array instead
# of adding smaller sub arrays, making for an easier join.