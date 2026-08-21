class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        total = 0
        def dfs(i):
            total = sum(subset)
            if i > len(nums) - 1 or total > target:
                return

            if total == target:
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i)
            subset.pop()
            dfs(i+1)
        dfs(0)

        return res