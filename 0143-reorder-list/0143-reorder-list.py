# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1-find mid node:
        fast,slow = head,head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 2-reverse second Half
        prev,curr = None,slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        # 3- Merge two linkedlist
        first,second = head, prev
        while second.next:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second =temp2
         


        