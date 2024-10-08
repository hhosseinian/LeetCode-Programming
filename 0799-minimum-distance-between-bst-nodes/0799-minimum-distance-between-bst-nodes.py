# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.prev_val = None
        self.min_diff = float('inf')
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            if self.prev_val is not None:
                diff = node.val-self.prev_val
                self.min_diff = min(self.min_diff,diff)
            self.prev_val = node.val
            dfs(node.right)
        dfs(root)
        return self.min_diff
