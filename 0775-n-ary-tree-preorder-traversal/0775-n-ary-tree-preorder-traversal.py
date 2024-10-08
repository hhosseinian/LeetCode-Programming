"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        self.preorder_stack = []
        def dfs(node):
            if not node:
                return
            self.preorder_stack.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return self.preorder_stack
        

        