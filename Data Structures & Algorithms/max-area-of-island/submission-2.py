class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        def dfs(row, col):
            if row < 0 or col < 0 or row > len(grid) - 1 or col > len(grid[0]) - 1 or grid[row][col] == 0:
                return 0

            grid[row][col] = 0 
            return (
                1 
                + dfs(row-1, col)
                + dfs(row+1, col)
                + dfs(row, col-1)
                + dfs(row, col+1) 
            )
            

        for row, _ in enumerate(grid):
            for col, __ in enumerate(grid[0]):
                if grid[row][col] == 1:
                    area = max(dfs(row, col), area)
        return area


            