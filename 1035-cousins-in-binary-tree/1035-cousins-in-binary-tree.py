# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x_depth = self.y_depth = -1
        self.xparent = self.yparent = None
        def dfs(node,parent,depth):
            if not node:
                return
            if node.val == x:
                self.x_depth = depth
                self.xparent = parent
            elif node.val == y:
                self.y_depth = depth
                self.yparent = parent
            dfs(node.left,node,depth+1)
            dfs(node.right,node,depth+1)
        dfs(root,None,0)
        return (self.x_depth == self.y_depth) and (self.xparent != self.yparent)

