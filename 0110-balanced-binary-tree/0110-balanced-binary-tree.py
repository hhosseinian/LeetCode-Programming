# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_height(node)->bool:
            if not node:
                return 0,True
            left_height,left_balanced = check_height(node.left)
            right_height,right_balanced = check_height(node.right)
            current_balance = left_balanced and right_balanced and abs(left_height-right_height) <=1
            return max(left_height,right_height)+1,current_balance
        height,balanced = check_height(root)
        return balanced
            
        