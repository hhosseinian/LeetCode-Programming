# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        def Inorder_Traverse(node):
            if not node:
                return
            Inorder_Traverse(node.left)
            values.append(node.val)
            Inorder_Traverse(node.right)
        Inorder_Traverse(root)
        mindiff = float('inf')
        for i in range(1,len(values)):
            diff = values[i]-values[i-1]
            mindiff = min(mindiff,diff)
        return mindiff
        