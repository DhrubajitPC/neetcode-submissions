# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        l1 = head
        l2 = head

        while l2 and l2.next:
            l1 = l1.next
            l2 = l2.next.next
        
        l2 = l1.next
        l1.next = None
        l1 = head

        p = None
        while l2:        
            n = l2.next
            l2.next = p
            p = l2
            l2 = n
        l2 = p

        while l1 and l2:
            n1 = l1.next
            n2 = l2.next

            l1.next = l2
            l2.next = n1

            l1 = n1

            l2 = n2
        
