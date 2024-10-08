# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        newroot = TreeNode(0)
        curr = newroot
        stack = deque()
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            curr.right = TreeNode(node.val)
            curr = curr.right
            node = node.right
        return newroot.right

        