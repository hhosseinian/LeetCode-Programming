# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the midpoint using slow/fast ptr
        fast,slow=head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # Reverse the second half
        prev,curr = None,slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # find Optimum traversing on first and second half
        first,second = head,prev
        max_Twin_Sum = 0
        while second:
            max_Twin_Sum = max(max_Twin_Sum, first.val + second.val)
            first = first.next
            second = second.next
        return max_Twin_Sum