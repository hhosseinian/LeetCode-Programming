# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total_sum = 0
        paths = []
        def dfs(node: Optional[TreeNode],path: str):
            if not node:
                return
            path+=str(node.val)
            if not node.left and not node.right:
                paths.append(path)
            else:
                dfs(node.left,path)
                dfs(node.right,path)
        dfs(root,"")
        for p in paths:
            total_sum+=int(p,2)
        return total_sum


        