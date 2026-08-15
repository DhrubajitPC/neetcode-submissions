class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
        # max_p = 0        
        # for i in range(len(prices)-1):
        #     for j in range(i, len(prices)):
        #         p = prices[j] - prices[i]
        #         max_p = max(max_p, p)
        # return max_p