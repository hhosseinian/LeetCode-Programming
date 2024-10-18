# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        def BFS(root:TreeNode)-> bool: 
            queue = deque([(0,root)])
            curr_val = None
            while queue:
                prev_val = None
                queue_size = len(queue)
                for i in range(queue_size):
                    index, node = queue.popleft()
                    curr_val = node.val
                    if index%2 == 0:
                        if curr_val % 2 == 0 or (prev_val is not None and curr_val<=prev_val):
                            return False
                    else:
                        if curr_val%2 == 1 or (prev_val is not None and curr_val>=prev_val):
                            return False
                    if node.left:
                        queue.append((index+1,node.left))
                    if node.right:
                        queue.append((index+1,node.right))
                    prev_val = curr_val
            return True
        return BFS(root)
                    
                


        