"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        levels = []
        def BFS(root):
            queue = deque([root])
            while queue:
                level = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    for child in node.children:
                        queue.append(child)
                levels.append(level)
        BFS(root)
        return levels

        