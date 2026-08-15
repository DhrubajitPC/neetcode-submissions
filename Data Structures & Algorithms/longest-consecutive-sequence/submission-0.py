class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        res = 0
        for x in num_set:
            current_num = x
            current_streak = 1
            while(current_num + 1) in num_set:
                current_num += 1
                current_streak += 1
            res = max(res, current_streak)
        return res
        
                
