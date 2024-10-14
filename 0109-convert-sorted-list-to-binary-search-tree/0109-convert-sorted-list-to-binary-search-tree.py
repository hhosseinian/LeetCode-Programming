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
        def find_size(node: Optional[ListNode])->int:
            size = 0
            while node:
                size+=1
                node = node.next
            return size
        def balanced_tree(left:int,right:int) -> Optional[TreeNode]:
            nonlocal head
            if left>right:
                return None
            mid =(left+right)//2
            left_child = balanced_tree(left,mid-1)
            root = TreeNode(head.val)
            root.left = left_child
            head = head.next
            root.right = balanced_tree(mid+1,right)
            return root
        return balanced_tree(0,find_size(head)-1)
 