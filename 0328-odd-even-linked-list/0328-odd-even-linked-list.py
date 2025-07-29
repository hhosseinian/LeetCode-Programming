# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head
        #n = 1
        Odd_pntr = head
        Even = head.next
        even_pntr = Even
        while Odd_pntr.next and even_pntr.next:
            Odd_pntr.next = even_pntr.next
            Odd_pntr = Odd_pntr.next
            even_pntr.next = Odd_pntr.next
            even_pntr = even_pntr.next
        Odd_pntr.next = Even
        return head
        
        