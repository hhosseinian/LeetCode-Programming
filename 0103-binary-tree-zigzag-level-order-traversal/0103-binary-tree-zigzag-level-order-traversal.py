# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue =deque([root])
        RtoL = True
        results = []
        while queue:
            level_size = len(queue)
            level_elements = []
            for i in range(level_size):
                node =queue.popleft()
                level_elements.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if RtoL:
                results.append(level_elements)
                RtoL = False
            else:
                results.append(reversed(level_elements))
                RtoL = True
        return results
