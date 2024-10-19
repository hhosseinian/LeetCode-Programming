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
        def DFS(node,depth):
            nonlocal levels_max
            if not node:
                return
            if depth == len(levels_max):
                levels_max.append(node.val)
            else:
                levels_max[depth] = max(levels_max[depth],node.val)
            DFS(node.left, depth+1)
            DFS(node.right, depth+1)

        DFS(root,0)
        return levels_max
        