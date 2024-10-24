class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        def dfs(i , j):
            # Check that we are in bounds, check that it is land, if not return
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                return
            # We can mark visited land by marking it as water
            grid[i][j] = '0'

            # Explore all four possible directions (up, down, left, right)
            dfs(i - 1, j)  # Up
            dfs(i + 1, j)  # Down
            dfs(i, j - 1)  # Left
            dfs(i, j + 1)  # Right

        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':  # Found an unvisited land
                    dfs(i, j)  # Perform DFS to mark the whole island
                    num_islands += 1  # Increment the island count

        return num_islands