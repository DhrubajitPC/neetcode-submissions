# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        def dfs(node: Optional[TreeNode], count: int) -> int:
            if not node:
                return count
            count += 1
            return max(dfs(node.left, count), dfs(node.right, count))
        count = max(count, dfs(root, 0))
        return count
