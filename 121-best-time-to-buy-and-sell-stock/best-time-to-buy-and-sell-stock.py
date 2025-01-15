class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        start = prices[0]
        for i in range(n):
            close = prices[i]
            if (prices[i] < start):
                start = prices[i]
            profit_i = close - start
            if (profit_i > profit):
                profit = profit_i
        return profit
                