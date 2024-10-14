# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        stack = []
        while head:
            stack.append(head.val)
            head=head.next
        def balanced_tree(stack:list)-> Optional[TreeNode]:
            n = len(stack)
            if n == 0:
                return
            root = TreeNode(stack[n//2])
            root.left = balanced_tree(stack[:n//2])
            root.right = balanced_tree(stack[n//2+1:])
            return root
        return balanced_tree(stack)