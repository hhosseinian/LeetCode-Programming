# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_linked_list(start: ListNode, k: int) -> ListNode:
            prev = None
            current = start
            for _ in range(k):
                next_node = current.next
                current.next = prev
                prev = current
                current = next_node
            return prev
        count = 0
        current =head
        while current:
            count+=1
            current =current.next
        dummy =ListNode(0)
        dummy.next = head
        group_prev =dummy
        while count>=k:
            group_start = group_prev.next
            group_end = group_start
            for _ in range(k-1): 
                group_end = group_end.next
            next_group_start = group_end.next
            group_prev.next = reverse_linked_list(group_start,k)
            group_start.next = next_group_start
            group_prev = group_start
            count -=k
        return dummy.next
            

