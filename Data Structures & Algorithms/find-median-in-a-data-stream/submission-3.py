class MedianFinder:

    def __init__(self):
        self.small = []
        self.big = []

    def addNum(self, num: int) -> None:
        if not self.small or num <= self.small[0]:
            heapq.heappush_max(self.small, num)
        else:
            heapq.heappush(self.big, num)
        
        if len(self.small) > len(self.big) + 1:
            val = heapq.heappop_max(self.small)
            heapq.heappush(self.big, val)

        elif len(self.big) > len(self.small) + 1:
            val = heapq.heappop(self.big)
            heapq.heappush_max(self.small, val)



    def findMedian(self) -> float:
        if len(self.big) > len(self.small):
            return self.big[0]
        elif len(self.small) > len(self.big):
            return self.small[0]
        else:
            return (self.big[0] + self.small[0]) / 2
        