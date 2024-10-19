# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        levels_max = []
        def BFS(node):
            nonlocal levels_max
            if not node:
                return
            queue = deque([node])
            while queue:
                curr_level_max = float('-inf')
                queue_size = len(queue)
                for _ in range(queue_size):
                    node = queue.popleft()
                    curr_level_max = max(curr_level_max,node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                levels_max.append(curr_level_max)
        BFS(root)
        return levels_max
        