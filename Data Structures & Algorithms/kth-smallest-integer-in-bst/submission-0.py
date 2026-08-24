# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return

        res = root.val
        def dfs(node):
            nonlocal res, k
            if not node:
                return
            
            dfs(node.left)
            if k == 0:
                return
            k -=1
            if k==0:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res


