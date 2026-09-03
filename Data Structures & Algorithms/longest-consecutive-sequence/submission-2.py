class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        memo = set(nums)
        
        start = []
        for i in nums:
            if i-1 not in memo:
                start.append(i)
        
        maxCount = 0
        for s in start:
            count = 0
            num = s

            while num in memo:
                count +=1
                num += 1
            maxCount = max(maxCount, count)
        
        return maxCount
            