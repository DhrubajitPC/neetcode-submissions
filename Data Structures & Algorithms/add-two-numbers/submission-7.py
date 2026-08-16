# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        head = dummy
        while l2 and l1:
            mySum = l1.val + l2.val + carry
            dummy.next = ListNode()
            if mySum <= 9:
                dummy.next.val = mySum
                carry = 0
            else:
                dummy.next.val = mySum % 10
                carry = 1
            l1 = l1.next
            l2 = l2.next
            dummy = dummy.next
        
        if not l2: 
            while l1:
                mySum = carry + l1.val
                if mySum > 9:
                    carry = 1
                else:
                    carry = 0
                dummy.next = ListNode()
                dummy.next.val = mySum % 10
                l1 = l1.next
                dummy = dummy.next
        if not l1:
            while l2:
                mySum = carry + l2.val
                if mySum > 9:
                    carry = 1
                else:
                    carry = 0
                dummy.next = ListNode()
                dummy.next.val = mySum % 10
                l2 = l2.next
                dummy = dummy.next

        if carry > 0:
            dummy.next = ListNode()
            dummy.next.val = carry
      
        return head.next
