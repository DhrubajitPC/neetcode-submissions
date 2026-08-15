class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = float('inf')
        for i in nums:
            if i < res:
                res = i
        return res