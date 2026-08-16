# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree is empty, it can't contain a subtree
        if not root:
            return False
        
        # If the trees are identical starting at this node, we found our subtree
        if self.isSameTree(root, subRoot):
            return True
        
        # Otherwise, keep searching recursively down the left and right branches
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, they match
        if not p and not q:
            return True
            
        # If only one is null, or if their values don't match, they aren't the same
        if not p or not q or p.val != q.val:
            return False
        
        # Recursively check that both the left and right subtrees are identical
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)