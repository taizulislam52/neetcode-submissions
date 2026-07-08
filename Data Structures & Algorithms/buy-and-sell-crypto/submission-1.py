class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        i = 0
        j = 1
        while i < len(prices):
            if j < len(prices) and prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxProfit = max(maxProfit, profit)
                j += 1
            else:
                i += 1
                j = i + 1
        
        return maxProfit
        