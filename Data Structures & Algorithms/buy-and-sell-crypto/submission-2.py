class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPriceSoFar = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            minPriceSoFar = min(prices[i], minPriceSoFar)
            currProfit = prices[i] - minPriceSoFar
            maxProfit = max(maxProfit, currProfit)
        return maxProfit
            