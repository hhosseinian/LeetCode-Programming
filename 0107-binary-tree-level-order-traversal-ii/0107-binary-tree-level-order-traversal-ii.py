# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levels = []
        def BFS(root: Optional[TreeNode])->None:
            nonlocal levels
            queue = deque([root])
            while queue:
                level = []
                for _ in range(len(queue)):
                    node = queue.popleft()
                    level.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                levels.insert(0,level)
        BFS(root)
        return levels
                

