class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in prices:
            profit = max(i - buy, profit)
            buy = min(buy, i)
        return profit