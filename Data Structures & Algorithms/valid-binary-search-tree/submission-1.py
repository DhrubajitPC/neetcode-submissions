# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def validateBST(node, upperBound, lowerBound):
            if not node:
                return True
                
            if (node.val >= upperBound or
                node.val <= lowerBound or
                (node.left and node.left.val >= node.val) or
                (node.right and node.right.val <= node.val)
            ):
                return False
            
            return True and validateBST(node.left, node.val, lowerBound) and validateBST(node.right, upperBound, node.val)
        
        return validateBST(root, float("inf"), float("-inf"))