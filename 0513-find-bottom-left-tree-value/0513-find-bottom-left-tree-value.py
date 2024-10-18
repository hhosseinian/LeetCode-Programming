# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        Bottom_Left = root.val
        def BFS(root:TreeNode)->None:
            nonlocal Bottom_Left
            queue = deque([root])
            while queue:
                queue_size = len(queue)
                Bottom_Left = queue[0].val
                for _ in range(queue_size):
                    node = queue.popleft()
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        BFS(root)
        return Bottom_Left
                
                    

