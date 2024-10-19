# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def DFS(node:TreeNode)->TreeNode:
            if not node:
                return None
            node.left = DFS(node.left)
            node.right = DFS(node.right)
            if target == node.val and not node.left and not node.right:
                return None
            return node
        
        return DFS(root)
                

