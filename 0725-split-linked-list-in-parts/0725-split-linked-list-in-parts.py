# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        result = [None]*k
        if not head:
            return result
        N = 0 #size
        curr = head
        while curr:
            N+=1
            curr = curr.next
        partsize = N//k
        extraone = N%k
        curr = head
        for i in range(k):
            result[i] = curr
            partition_size = partsize +(1 if i<extraone else 0)
            for j in range(partition_size-1):
                if curr:
                    curr = curr.next
            if curr:
                nxt = curr.next
                curr.next = None
            curr = nxt
        return result


