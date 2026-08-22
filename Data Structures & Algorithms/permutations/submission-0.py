class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = [False] * len(nums)
        stack = []
        def dfs(i, seen, stack):
            if len(stack) == len(nums):
                res.append(stack.copy())
                
            if i >= len(nums):
                return
            
            
            for j in range(len(nums)):
                if seen[j]:
                    continue
                seen[j] = True
                stack.append(nums[j])
                dfs(i+1, seen, stack)
                stack.pop()
                seen[j] = False
        
        dfs(0, seen, stack)

        return res
            