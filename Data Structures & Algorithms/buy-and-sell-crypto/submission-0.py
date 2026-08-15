class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                p = prices[j] - prices[i]
                max_p = max(max_p, p)
        return max_p