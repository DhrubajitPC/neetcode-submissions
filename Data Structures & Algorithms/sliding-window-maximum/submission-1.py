import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        heap = nums[:k]
        heapq.heapify_max(heap)
        for r in range(k-1, len(nums)):
            heap = nums[l:r+1]
            heapq.heapify_max(heap)
            # print(f"window {nums[l:r+1]}")
            # print(f"heap {heap}")
            
            # heap = nums[l:r+1].copy()
            # heapq.heapify_max(heap)
            # heapq.heappush_max(heap, nums[r])
            max = heapq.heappop_max(heap)
            res.append(max)
            # print(f"res {res}")
            # heapq.heappush_max(heap, nums[r])
            # print(f"new window {nums[l:r]}")
            # print(f"updated heap {heap}")
            l+=1
        
        return res
