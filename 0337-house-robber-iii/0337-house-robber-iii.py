# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def DFS(node):
            if not node:
                return (0,0)
            left = DFS(node.left)
            right = DFS(node.right)
            rob_this = node.val+left[0]+right[0]
            not_robing_this = max(left)+max(right)
            return (not_robing_this,rob_this)
        return max(DFS(root))
            