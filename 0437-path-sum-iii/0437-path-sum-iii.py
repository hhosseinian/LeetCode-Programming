# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        total_paths = 0
        def dfs(node,curr_sum)->int:
            if not node:
                return 0
            curr_sum +=node.val
            count = 1 if curr_sum == targetSum else 0
            count += dfs(node.left,curr_sum)
            count += dfs(node.right,curr_sum)
            return count
        def countpath(node):
            nonlocal total_paths
            if not node:
                return
            total_paths+=dfs(node,0)
            countpath(node.left)
            countpath(node.right)
        countpath(root)
        return total_paths

            

        