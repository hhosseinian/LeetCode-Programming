# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")
        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0
            left_max = max(dfs(node.left),0)
            right_max = max(dfs(node.right),0)
            current_max = left_max + node.val + right_max
            max_sum = max(current_max,max_sum)
            return node.val + max(left_max,right_max)
        dfs(root)
        return max_sum
        