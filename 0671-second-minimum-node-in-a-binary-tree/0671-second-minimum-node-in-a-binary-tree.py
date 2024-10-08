# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        self.min_val = [float('inf')]*2
        def dfs(node):
            if not node:
                return
            if node.val<self.min_val[0]:
                self.min_val[1] = self.min_val[0]
                self.min_val[0] = node.val
            elif self.min_val[0]<node.val<self.min_val[1]:
                self.min_val[1] = node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.min_val[1] if self.min_val[1]<float('inf') else -1


        