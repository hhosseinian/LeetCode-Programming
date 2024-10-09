# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        total_paths = 0
        def dfs(node,curr_sum,prefix_sum)->int:
            if not node:
                return 0
            curr_sum +=node.val
            count = prefix_sum.get(curr_sum-targetSum,0)
            prefix_sum[curr_sum] = prefix_sum.get(curr_sum,0)+1
            count += dfs(node.left,curr_sum,prefix_sum)
            count += dfs(node.right,curr_sum,prefix_sum)
            prefix_sum[curr_sum]-=1
            if prefix_sum[curr_sum] == 0:
                del prefix_sum[curr_sum]
            return count
        prefix_sum = {0: 1}
        return dfs(root,0,prefix_sum)

            

        