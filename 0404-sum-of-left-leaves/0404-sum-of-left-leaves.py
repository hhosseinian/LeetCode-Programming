# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        if root is None:
            return 0
        if root.left and not root.left.left and not root.left.right:
            result += root.left.val
        result+=self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)
        return result
        
        