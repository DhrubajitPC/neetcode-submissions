class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for k, v in enumerate(nums):
            if k > 0 and v == nums[k-1]:
                continue

            l = k + 1
            r = len(nums) - 1
            while l < r:
                total = v + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return res