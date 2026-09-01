class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, v in enumerate(temperatures):
            if stack and stack[-1][0] < v:
                while stack and stack[-1][0] < v:
                    _, lastIdx = stack.pop()
                    res[lastIdx] = i - lastIdx
            stack.append((v, i))
        return res