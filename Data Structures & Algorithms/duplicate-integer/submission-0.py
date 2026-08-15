class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for i in nums:
            if i not in memo:
                memo[i] = 1
            else:
                return True
        return False
        