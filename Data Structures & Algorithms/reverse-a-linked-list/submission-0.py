# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
            
        p,c = None, head
        while c.next:
            n = c.next
            c.next = p
            p = c
            c = n
        c.next = p
        return c