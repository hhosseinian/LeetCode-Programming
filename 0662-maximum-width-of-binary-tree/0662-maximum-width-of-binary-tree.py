# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_width = 0
        def BFS(root: TreeNode)->None:
            nonlocal max_width
            queue = deque([(0,root)]) # node index, node
            while queue:
                level_width = 0
                queue_size = len(queue)
                first_index,_ = queue[0]
                for _ in range(queue_size):
                    index, node = queue.popleft()
                    if node.left:
                        queue.append((2*index,node.left))
                    if node.right:
                        queue.append((2*index+1,node.right))
                max_width = max(max_width,index -first_index+1)
        BFS(root)
        return max_width
                
        