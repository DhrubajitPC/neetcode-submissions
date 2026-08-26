from typing import List


class TrieNode:
    def __init__(self):
        self.word = None
        self.children = {}


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []

        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word

        rows = len(board)
        cols = len(board[0])

        res = []

        def dfs(node: TrieNode, row: int, col: int):
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] == "#"
                or board[row][col] not in node.children
            ):
                return

            char = board[row][col]
            next_node = node.children[char]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = None

            board[row][col] = "#"

            dfs(next_node, row - 1, col)
            dfs(next_node, row + 1, col)
            dfs(next_node, row, col - 1)
            dfs(next_node, row, col + 1)

            board[row][col] = char

        for row in range(rows):
            for col in range(cols):
                dfs(root, row, col)
        return res

