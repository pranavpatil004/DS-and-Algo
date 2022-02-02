# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        for i in range(0,n):
            temp = temp.next
        i = head
        while temp.next:
            temp = temp.next
            i = i.next
        i = i.next.next if i.next else None
        return head
    

head
Solution().removeNthFromEnd([1,2,3,4,5], 2)