# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def height(node, count = 0):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            if left == -1 or right == -1:
                return -1

            diff = abs(left - right)
            if diff > 1 :
                return -1

            return 1 + max(height(node.left), height(node.right))

        left = height(root.left)
        right = height(root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return False
        else:
            return True
