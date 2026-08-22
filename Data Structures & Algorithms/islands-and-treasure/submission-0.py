from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def add_cell(r,c):
            if (min(r, c) < 0 or 
                r >= rows or  
                c >= cols or  
                (r,c) in visit or 
                grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    visit.add((row,col))
                    q.append([row,col])
        dist = 0
        while q:
            for level in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                add_cell(r-1,c)
                add_cell(r,c+1)
                add_cell(r+1,c)
                add_cell(r,c-1)
            dist+=1
        