class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        memo = {}
        def dfs(i, j, grid):
            if i<0 or j <0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] == "0":
                return

            key = f"{i}{j}"
            if key not in memo:
                memo[key] = "visited"
            else:
                return
            
            dfs(i-1, j, grid)
            dfs(i+1, j, grid)
            dfs(i, j-1, grid)
            dfs(i, j+1, grid)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0':
                    continue
                key = f"{row}{col}"
                if key not in memo:
                    # print(key)
                    dfs(row, col, grid)
                    # print(memo)
                    count+=1
                    # print(count)
        return count
