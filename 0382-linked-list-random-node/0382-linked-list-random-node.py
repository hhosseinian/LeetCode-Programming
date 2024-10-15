# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import random
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.size = 0
        while head:
            head = head.next
            self.size+=1
    def getRandom(self) -> int:
        index = random.randint(0,self.size-1)
        node = self.head
        for _ in range(index):
            node =node.next
        return node.val

        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()