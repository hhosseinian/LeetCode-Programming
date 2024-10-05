# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def in_order_traversal(node):
            if not node:
                return []
            return in_order_traversal(node.left)+[node.val]+in_order_traversal(node.right)
        elements = in_order_traversal(root)
        return elements[k-1]
