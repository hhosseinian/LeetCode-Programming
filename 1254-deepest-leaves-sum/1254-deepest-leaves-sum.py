# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        Deepest_sum = 0
        def BFS(root)->None:
            queue = deque([root])
            nonlocal Deepest_sum
            while queue:
                Deepest_sum = 0
                queue_size = len(queue)
                for _ in range(queue_size):
                    node = queue.popleft()
                    Deepest_sum+=node.val
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
        BFS(root)
        return Deepest_sum

                

