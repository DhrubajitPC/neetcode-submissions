# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        res = [root.val]
        q.append([root])
        while q:
            current_level = q.popleft()
            new_level = []
            for l in current_level:
                if l.left:
                    new_level.append(l.left)
                if l.right:
                    new_level.append(l.right)
            if len(new_level) > 0:
                q.append(new_level)
                res.append(new_level[-1].val)
        

        return res
        
