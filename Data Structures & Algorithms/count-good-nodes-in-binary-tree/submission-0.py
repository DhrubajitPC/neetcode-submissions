# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cur_max = root.val
        res = 0

        def dfs(node, max_val):
            if not node:
                return 0
            
            new_max = max(max_val, node.val)
            
            
            if node.val >= max_val:
                return 1 + dfs(node.left, new_max) + dfs(node.right, new_max)
            else:
                return 0 + dfs(node.left, new_max) + dfs(node.right, new_max)
        
        res += dfs(root, root.val)
        return res

