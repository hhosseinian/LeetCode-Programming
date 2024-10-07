# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap =[]
        for index,lst in enumerate(lists):
            if lst:
                heapq.heappush(min_heap,(lst.val,index,lst))
        dummy = ListNode(0)
        current =dummy
        while min_heap:
            val,index,node =heapq.heappop(min_heap)
            current.next = ListNode(val)
            current = current.next
            if node.next:
                heapq.heappush(min_heap,(node.next.val,index,node.next))
        return dummy.next
                
