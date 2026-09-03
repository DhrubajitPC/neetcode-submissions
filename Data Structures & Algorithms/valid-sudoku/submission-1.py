class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidRows(board) and self.isValidCols(board) and self.isValidBox(board)
    
    def isValidRows(self, board):
        for row in board:
            seen = set()
            for col in row:
                if col == ".":
                    continue
                if col in seen:
                    return False
                else:
                    seen.add(col) 
        return True
    
    def isValidCols(self, board):
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in seen:
                    return False
                else:
                    seen.add(board[row][col]) 
        return True
    
    def isValidBox(self, board):
        boundaries = [
            [[0,0], [2,2]],
            [[0,3], [2,5]],
            [[0,6], [2,8]],
            [[3,0], [5,2]],
            [[3,3], [5,5]],
            [[3,6], [5,8]],
            [[6,0], [8,2]],
            [[6,3], [8,5]],
            [[6,6], [8,8]]
        ]

        for bound in boundaries:
            start, end = bound
            seen = set()
            for row in range(start[0], end[0]+1):
                for col in range(start[1], end[1]+1):
                    if board[row][col] == ".":
                        continue

                    if board[row][col] in seen:
                        return False
                    else:
                        seen.add(board[row][col]) 
        return True

    