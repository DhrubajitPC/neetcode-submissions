import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify_max(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        x =  heapq.nlargest(self.k, self.heap)
        return x[-1]
