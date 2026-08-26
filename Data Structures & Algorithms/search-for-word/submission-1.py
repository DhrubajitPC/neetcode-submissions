from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def startSearch(word, charIndex, row, col, board):
            # path = []
            if not charIndex < len(word):
                return True

            if not (0 <= row < len(board) and 0 <= col < len(board[0])):
                return False

            if not board[row][col] == word[charIndex]:
                return False
            
            temp = board[row][col]
            board[row][col] = "#"

            searchUp = startSearch(word, charIndex + 1, row - 1, col, board)
            searchDown = startSearch(word, charIndex + 1, row + 1, col, board)
            searchLeft = startSearch(word, charIndex + 1, row, col - 1, board)
            searchRight = startSearch(word, charIndex + 1, row, col + 1, board)

            board[row][col] = temp
            return searchUp or searchDown or searchLeft or searchRight

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    res = startSearch(word, 0, r, c, board)
                    if res:
                        return True

        return False
