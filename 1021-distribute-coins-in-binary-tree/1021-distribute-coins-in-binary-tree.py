# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        if not root.left and not root.right:
            return 0
        def DFS(node)->int:
            if not node:
                return 0
            left = DFS(node.left)
            right = DFS(node.right)
            self.moves+=abs(left)+abs(right)
            return node.val-1+ left+right
        DFS(root)
        return self.moves
