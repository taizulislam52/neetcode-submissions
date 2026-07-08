class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0

        for i in range(len(prices)):
            buyPrice = prices[i]
            for j in range(i+1, len(prices)):
                sellPrice = prices[j]
                if buyPrice < sellPrice:
                    profit = sellPrice - buyPrice
                    maxProfit = max(maxProfit, profit)
        
        return maxProfit

        