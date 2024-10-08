# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.newroot = TreeNode(0)
        self.curr = self.newroot
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.curr.right = TreeNode(node.val)
            self.curr = self.curr.right
            dfs(node.right)
        dfs(root)
        return self.newroot.right
        