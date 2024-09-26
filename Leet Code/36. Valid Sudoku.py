class Solution(object):
    def isValidSudoku(self, board):
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        return len(res) == len(set(res))

# Initial solution
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for row in board:
#             row_dict = {}
#             for num in row:
#                 if num != "." and num in row_dict:
#                     print("row")
#                     print("Num: ", num)
#                     return False
#                 else:
#                     row_dict[num] = 1
#         for i in range(9):
#             print("new col")
#             col_dict = {}
#             for j in range(9):
#                 print("colnum: ", board[j][i])
#                 print("coldict: ", col_dict)
#                 if board[j][i] != "." and board[j][i] in col_dict:
#                     print("Col")
#                     return False
#                 else:
#                     col_dict[board[j][i]] = 1
#         # Outer loop iterates over the top-left corner of each 3x3 box
#         for box_row in range(0, 8, 3):  # Iterate over box rows (0, 3, 6)
#             for box_col in range(0, 8, 3):  # Iterate over box columns (0, 3, 6)
#                 box_dict = {}
#                 # Inner loop iterates over each cell in the current 3x3 box
#                 for i in range(3):  # Iterate over rows within the 3x3 box
#                     for j in range(3):  # Iterate over columns within the 3x3 box
#                         # Access the element at board[box_row + i][box_col + j]
#                         # print("boxnum: ", board[box_row + i][box_col + j])
#                         if board[box_row + i][box_col + j] != "." and board[box_row + i][box_col + j] in box_dict:
#                             print("Box")
#                             return False
#                         else:
#                             box_dict[board[box_row + i][box_col + j]] = 1
#         return True