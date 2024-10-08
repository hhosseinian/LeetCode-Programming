"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        postorder_stack = []
        def dfs(node):
            for child in node.children:
                dfs(child)
            postorder_stack.append(node.val)
        dfs(root)
        return postorder_stack
        

        