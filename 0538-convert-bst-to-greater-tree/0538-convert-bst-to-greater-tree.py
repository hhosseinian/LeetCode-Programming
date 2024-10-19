# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        total_sum = 0
        def reverse_inorder(node):
            nonlocal total_sum
            if not node:
                return
            reverse_inorder(node.right)
            total_sum += node.val
            node.val = total_sum
            reverse_inorder(node.left)
        reverse_inorder(root)
        return root



            

        