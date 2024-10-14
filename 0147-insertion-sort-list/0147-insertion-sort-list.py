# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        sorted_head = ListNode(0)
        curr = head
        while curr:
            prev = sorted_head
            nxt = curr.next
            while prev.next and prev.next.val<curr.val:
                prev = prev.next
            curr.next = prev.next
            prev.next = curr
            curr = nxt
        return  sorted_head.next
            

        