"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
      
        memo = {}
        def dfs(node):
            if node.val in memo:
                return memo[node.val]
            newNode = Node(node.val)
            memo[node.val] = newNode
            for c in node.neighbors:
                # copy child here and return
                copied_c = dfs(c)
                newNode.neighbors.append(copied_c)
            
            return newNode

        return dfs(node)
        # return root
