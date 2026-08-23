# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter+=1
        if not heap:
            return
            
        _, _, head = heapq.heappop(heap)
        if head.next:
            heapq.heappush(heap, (head.next.val, counter, head.next))
            counter+=1

        cur = head
        while len(heap) > 0:
            _, _, node = heapq.heappop(heap)
            cur.next = node
            cur = cur.next
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter+=1

        
        return head