# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        rootval = postorder.pop()
        ind = inorder.index(rootval)
        root = TreeNode(rootval)
        root.right = self.buildTree(inorder[ind+1:],postorder)
        root.left = self.buildTree(inorder[:ind],postorder)
        
        return root

        