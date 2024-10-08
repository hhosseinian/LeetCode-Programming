# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        val = root.val
        def check(node):
            if not node:
                return True
            return node.val == val and check(node.left) and check(node.right)
        return check(root)
        