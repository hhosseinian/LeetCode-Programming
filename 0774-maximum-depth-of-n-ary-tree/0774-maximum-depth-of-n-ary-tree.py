"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(node) -> int:
            children_depth = set([0])
            if not node:
                return 0
            for child in node.children:
                children_depth.add(dfs(child)+1)
            return max(children_depth)
        
        return dfs(root)+1
            
            
