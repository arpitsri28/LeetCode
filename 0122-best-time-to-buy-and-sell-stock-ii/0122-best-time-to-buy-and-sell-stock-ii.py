class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        s = prices[0]
        profit = 0
        n = len(prices)
        if n == 1:
            return profit
        for i in range(1, n):
            if prices[i] - s > 0:
                profit += prices[i] - s
            s = prices[i]
        
        return profit
        