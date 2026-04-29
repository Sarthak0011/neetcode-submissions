class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        minPriceSoFar = prices[0]

        for i in range(1, n):
            currProfit = prices[i] - minPriceSoFar
            maxProfit = max(maxProfit, currProfit)
            if prices[i] <= minPriceSoFar:
                minPriceSoFar = prices[i]
        
        return maxProfit
        