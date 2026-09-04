from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    q.append((row, col))
        count = 0
        
        while q:
            rotted = False
            for i in range(len(q)):
                r,c = q.popleft()

                neighbors = [
                    (r, c+1),
                    (r+1, c),
                    (r, c-1),
                    (r-1, c)
                ]

                for n in neighbors:
                    nr, nc = n
                    if (
                        0<=nr<len(grid) and
                        0<=nc<len(grid[0]) and
                        grid[nr][nc] == 1
                    ):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        rotted = True
                
            if rotted:
                count+=1
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    return -1
        
        return count
        